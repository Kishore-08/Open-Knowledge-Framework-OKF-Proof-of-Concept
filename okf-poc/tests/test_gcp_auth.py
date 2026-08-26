from datetime import datetime, timezone
from unittest.mock import Mock, patch

from app.core import gcp_auth
from app.core.gcp_auth import GcloudImpersonatedCredentials, TokenFileCredentials


def test_gcloud_impersonated_credentials_refreshes_token_in_memory():
    credentials = GcloudImpersonatedCredentials(
        "vertex-runtime@example-project.iam.gserviceaccount.com"
    )
    completed = Mock(returncode=0, stdout="generated-token\n", stderr="")

    with patch("app.core.gcp_auth.shutil.which", return_value="/usr/bin/gcloud"):
        with patch("app.core.gcp_auth.subprocess.run", return_value=completed) as run:
            credentials.refresh(request=None)

    assert credentials.token == "generated-token"
    assert credentials.expiry is not None
    assert run.call_args.args[0] == [
        "/usr/bin/gcloud",
        "auth",
        "print-access-token",
        "--impersonate-service-account=vertex-runtime@example-project.iam.gserviceaccount.com",
        "--quiet",
    ]


def test_gcloud_impersonated_credentials_does_not_expose_stdout_on_failure():
    credentials = GcloudImpersonatedCredentials(
        "vertex-runtime@example-project.iam.gserviceaccount.com"
    )
    completed = Mock(returncode=1, stdout="sensitive-output", stderr="denied")

    with patch("app.core.gcp_auth.shutil.which", return_value="/usr/bin/gcloud"):
        with patch("app.core.gcp_auth.subprocess.run", return_value=completed):
            try:
                credentials.refresh(request=None)
            except RuntimeError as exc:
                assert "sensitive-output" not in str(exc)
                assert "denied" in str(exc)
            else:
                raise AssertionError("Expected refresh failure")


def test_token_file_credentials_uses_sidecar_creation_time(tmp_path):
    created_at = int(datetime.now(timezone.utc).timestamp())
    token_file = tmp_path / "credentials"
    token_file.write_text(f"{created_at}\nsidecar-token\n", encoding="utf-8")

    credentials = TokenFileCredentials(str(token_file))
    credentials.refresh(request=None)

    assert credentials.token == "sidecar-token"
    assert credentials.expiry is not None


def test_token_file_takes_precedence_over_stale_explicit_token(tmp_path):
    token_file = tmp_path / "credentials"
    token_file.write_text("1\nsidecar-token\n", encoding="utf-8")

    with patch.object(gcp_auth.settings, "VERTEX_ACCESS_TOKEN_FILE", str(token_file)):
        with patch.object(gcp_auth.settings, "VERTEX_ACCESS_TOKEN", "stale-token"):
            credentials = gcp_auth.get_vertex_credentials()

    assert isinstance(credentials, TokenFileCredentials)


def test_token_file_credentials_adopts_sidecar_rotation_before_expiry(tmp_path):
    token_file = tmp_path / "credentials"
    token_file.write_text("100\nold-token\n", encoding="utf-8")
    credentials = TokenFileCredentials(str(token_file))
    credentials.refresh(request=None)

    token_file.write_text("200\nnew-token\n", encoding="utf-8")
    headers = {}
    credentials.before_request(None, "POST", "https://example.test", headers)

    assert credentials.token == "new-token"
    assert headers["authorization"] == "Bearer new-token"
