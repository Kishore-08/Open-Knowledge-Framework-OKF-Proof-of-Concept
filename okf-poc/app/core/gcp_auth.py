import shutil
import subprocess
from datetime import datetime, timedelta, timezone
from pathlib import Path

import google.auth
from google.auth.credentials import Credentials
from google.oauth2.credentials import Credentials as AccessTokenCredentials

from app.core.config import settings

_CLOUD_PLATFORM_SCOPE = "https://www.googleapis.com/auth/cloud-platform"
_GCLOUD_TOKEN_LIFETIME = timedelta(minutes=50)
_GCLOUD_TIMEOUT_SECONDS = 30


class GcloudImpersonatedCredentials(Credentials):
    """Refreshable credentials backed by an authenticated local gcloud CLI."""

    def __init__(self, service_account_email: str) -> None:
        super().__init__()
        self.service_account_email = service_account_email
        self.token = None
        self.expiry = None

    def refresh(self, request) -> None:  # noqa: ARG002 - google-auth interface
        gcloud = shutil.which("gcloud")
        if not gcloud:
            raise RuntimeError(
                "VERTEX_SERVICE_ACCOUNT_EMAIL is configured, but gcloud was "
                "not found. Install gcloud and run the app on the authenticated "
                "host; the current Docker images do not include gcloud."
            )

        command = [
            gcloud,
            "auth",
            "print-access-token",
            f"--impersonate-service-account={self.service_account_email}",
            "--quiet",
        ]
        try:
            result = subprocess.run(
                command,
                check=False,
                capture_output=True,
                text=True,
                timeout=_GCLOUD_TIMEOUT_SECONDS,
            )
        except subprocess.TimeoutExpired as exc:
            raise RuntimeError(
                "Timed out while asking gcloud for a Vertex access token."
            ) from exc

        token = result.stdout.strip()
        if result.returncode != 0 or not token:
            detail = result.stderr.strip().splitlines()
            suffix = f" Last gcloud message: {detail[-1]}" if detail else ""
            raise RuntimeError(
                "gcloud could not impersonate the configured Vertex service "
                f"account.{suffix}"
            )

        self.token = token
        # Impersonated access tokens normally last one hour. Mark them as
        # expiring sooner so google-auth refreshes before the real deadline.
        self.expiry = (
            datetime.now(timezone.utc).replace(tzinfo=None)
            + _GCLOUD_TOKEN_LIFETIME
        )


class TokenFileCredentials(Credentials):
    """Credentials refreshed from a token file maintained by a sidecar."""

    def __init__(self, token_file: str) -> None:
        super().__init__()
        self.token_file = Path(token_file)
        self.token = None
        self.expiry = None

    def refresh(self, request) -> None:  # noqa: ARG002 - google-auth interface
        try:
            lines = self.token_file.read_text(encoding="utf-8").splitlines()
            created_at = int(lines[0])
            token = lines[1].strip()
        except (OSError, ValueError, IndexError) as exc:
            raise RuntimeError(
                "The Vertex token sidecar has not produced valid credentials "
                f"at {self.token_file}. Check: docker compose logs vertex-token"
            ) from exc

        if not token:
            raise RuntimeError("The Vertex token sidecar produced an empty token.")

        self.token = token
        self.expiry = (
            datetime.fromtimestamp(created_at, timezone.utc).replace(tzinfo=None)
            + _GCLOUD_TOKEN_LIFETIME
        )


def get_vertex_credentials() -> Credentials:
    """Resolve sidecar, explicit, gcloud, or default Vertex credentials."""
    settings.validate_vertex_config()

    # Docker explicitly configures this path. Prefer it over a stale manual
    # token that might still be present in .env during migration.
    token_file = (settings.VERTEX_ACCESS_TOKEN_FILE or "").strip()
    if token_file:
        return TokenFileCredentials(token_file)

    token = (settings.VERTEX_ACCESS_TOKEN or "").strip()
    if token and token not in {
        "your_vertex_access_token_here",
        "${VERTEX_ACCESS_TOKEN}",
    }:
        return AccessTokenCredentials(
            token=token,
            scopes=[_CLOUD_PLATFORM_SCOPE],
        )

    service_account_email = (
        settings.VERTEX_SERVICE_ACCOUNT_EMAIL or ""
    ).strip()
    if service_account_email and service_account_email not in {
        "service-account@project-id.iam.gserviceaccount.com",
        "${VERTEX_SERVICE_ACCOUNT_EMAIL}",
    }:
        return GcloudImpersonatedCredentials(service_account_email)

    credentials, _ = google.auth.default(scopes=[_CLOUD_PLATFORM_SCOPE])
    return credentials


# Backward-compatible name for existing imports.
get_service_account_credentials = get_vertex_credentials
