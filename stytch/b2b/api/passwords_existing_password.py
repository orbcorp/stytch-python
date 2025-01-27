# !!!
# WARNING: This file is autogenerated
# Only modify code within MANUAL() sections
# or your changes may be overwritten later!
# !!!

from __future__ import annotations

from typing import Any, Dict, Optional

from stytch.b2b.models.passwords_existing_password import ResetResponse
from stytch.core.api_base import ApiBase
from stytch.core.http.client import AsyncClient, SyncClient


class ExistingPassword:
    def __init__(
        self,
        api_base: ApiBase,
        sync_client: SyncClient,
        async_client: AsyncClient,
    ) -> None:
        self.api_base = api_base
        self.sync_client = sync_client
        self.async_client = async_client

    def reset(
        self,
        email_address: str,
        existing_password: str,
        new_password: str,
        organization_id: str,
        session_token: Optional[str] = None,
        session_duration_minutes: Optional[int] = None,
        session_jwt: Optional[str] = None,
        session_custom_claims: Optional[Dict[str, Any]] = None,
    ) -> ResetResponse:
        """Reset the member’s password using their existing password.

        This endpoint adapts to your Project's password strength configuration.
        If you're using [zxcvbn](https://stytch.com/docs/passwords#strength-requirements), the default, your passwords are considered valid
        if the strength score is >= 3. If you're using [LUDS](https://stytch.com/docs/passwords#strength-requirements), your passwords are
        considered valid if they meet the requirements that you've set with Stytch.
        You may update your password strength configuration in the [stytch dashboard](https://stytch.com/dashboard/password-strength-config).

        Fields:
          - email_address: The email address of the Member.
          - existing_password: The member's current password that they supplied.
          - new_password: The member's elected new password.
          - organization_id: Globally unique UUID that identifies a specific Organization. The `organization_id` is critical to perform operations on an Organization, so be sure to preserve this value.
          - session_token: A secret token for a given Stytch Session.
          - session_duration_minutes: Set the session lifetime to be this many minutes from now. This will start a new session if one doesn't already exist,
          returning both an opaque `session_token` and `session_jwt` for this session. Remember that the `session_jwt` will have a fixed lifetime of
          five minutes regardless of the underlying session duration, and will need to be refreshed over time.

          This value must be a minimum of 5 and a maximum of 527040 minutes (366 days).

          If a `session_token` or `session_jwt` is provided then a successful authentication will continue to extend the session this many minutes.

          If the `session_duration_minutes` parameter is not specified, a Stytch session will be created with a 60 minute duration. If you don't want
          to use the Stytch session product, you can ignore the session fields in the response.
          - session_jwt: The JSON Web Token (JWT) for a given Stytch Session.
          - session_custom_claims: Add a custom claims map to the Session being authenticated. Claims are only created if a Session is initialized by providing a value in
          `session_duration_minutes`. Claims will be included on the Session object and in the JWT. To update a key in an existing Session, supply a new value. To
          delete a key, supply a null value. Custom claims made with reserved claims (`iss`, `sub`, `aud`, `exp`, `nbf`, `iat`, `jti`) will be ignored.
          Total custom claims size cannot exceed four kilobytes.
        """  # noqa
        data: Dict[str, Any] = {
            "email_address": email_address,
            "existing_password": existing_password,
            "new_password": new_password,
            "organization_id": organization_id,
        }
        if session_token is not None:
            data["session_token"] = session_token
        if session_duration_minutes is not None:
            data["session_duration_minutes"] = session_duration_minutes
        if session_jwt is not None:
            data["session_jwt"] = session_jwt
        if session_custom_claims is not None:
            data["session_custom_claims"] = session_custom_claims

        url = self.api_base.url_for("/v1/b2b/passwords/existing_password/reset", data)
        res = self.sync_client.post(url, data)
        return ResetResponse.from_json(res.response.status_code, res.json)

    async def reset_async(
        self,
        email_address: str,
        existing_password: str,
        new_password: str,
        organization_id: str,
        session_token: Optional[str] = None,
        session_duration_minutes: Optional[int] = None,
        session_jwt: Optional[str] = None,
        session_custom_claims: Optional[Dict[str, Any]] = None,
    ) -> ResetResponse:
        """Reset the member’s password using their existing password.

        This endpoint adapts to your Project's password strength configuration.
        If you're using [zxcvbn](https://stytch.com/docs/passwords#strength-requirements), the default, your passwords are considered valid
        if the strength score is >= 3. If you're using [LUDS](https://stytch.com/docs/passwords#strength-requirements), your passwords are
        considered valid if they meet the requirements that you've set with Stytch.
        You may update your password strength configuration in the [stytch dashboard](https://stytch.com/dashboard/password-strength-config).

        Fields:
          - email_address: The email address of the Member.
          - existing_password: The member's current password that they supplied.
          - new_password: The member's elected new password.
          - organization_id: Globally unique UUID that identifies a specific Organization. The `organization_id` is critical to perform operations on an Organization, so be sure to preserve this value.
          - session_token: A secret token for a given Stytch Session.
          - session_duration_minutes: Set the session lifetime to be this many minutes from now. This will start a new session if one doesn't already exist,
          returning both an opaque `session_token` and `session_jwt` for this session. Remember that the `session_jwt` will have a fixed lifetime of
          five minutes regardless of the underlying session duration, and will need to be refreshed over time.

          This value must be a minimum of 5 and a maximum of 527040 minutes (366 days).

          If a `session_token` or `session_jwt` is provided then a successful authentication will continue to extend the session this many minutes.

          If the `session_duration_minutes` parameter is not specified, a Stytch session will be created with a 60 minute duration. If you don't want
          to use the Stytch session product, you can ignore the session fields in the response.
          - session_jwt: The JSON Web Token (JWT) for a given Stytch Session.
          - session_custom_claims: Add a custom claims map to the Session being authenticated. Claims are only created if a Session is initialized by providing a value in
          `session_duration_minutes`. Claims will be included on the Session object and in the JWT. To update a key in an existing Session, supply a new value. To
          delete a key, supply a null value. Custom claims made with reserved claims (`iss`, `sub`, `aud`, `exp`, `nbf`, `iat`, `jti`) will be ignored.
          Total custom claims size cannot exceed four kilobytes.
        """  # noqa
        data: Dict[str, Any] = {
            "email_address": email_address,
            "existing_password": existing_password,
            "new_password": new_password,
            "organization_id": organization_id,
        }
        if session_token is not None:
            data["session_token"] = session_token
        if session_duration_minutes is not None:
            data["session_duration_minutes"] = session_duration_minutes
        if session_jwt is not None:
            data["session_jwt"] = session_jwt
        if session_custom_claims is not None:
            data["session_custom_claims"] = session_custom_claims

        url = self.api_base.url_for("/v1/b2b/passwords/existing_password/reset", data)
        res = await self.async_client.post(url, data)
        return ResetResponse.from_json(res.response.status, res.json)
