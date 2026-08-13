import google.auth
from google.auth.credentials import Credentials
from google.oauth2.credentials import Credentials as AccessTokenCredentials

from app.core.config import settings

_CLOUD_PLATFORM_SCOPE = "https://www.googleapis.com/auth/cloud-platform"


def get_vertex_credentials() -> Credentials:
    """Use an explicit Vertex token when supplied, otherwise fall back to ADC."""
    settings.validate_vertex_config()

    token = (settings.VERTEX_ACCESS_TOKEN or "").strip()
    if token and token not in {
        "your_vertex_access_token_here",
        "${VERTEX_ACCESS_TOKEN}",
    }:
        return AccessTokenCredentials(
            token=token,
            scopes=[_CLOUD_PLATFORM_SCOPE],
        )

    credentials, _ = google.auth.default(scopes=[_CLOUD_PLATFORM_SCOPE])
    return credentials


# Backward-compatible name for existing imports.
get_service_account_credentials = get_vertex_credentials
