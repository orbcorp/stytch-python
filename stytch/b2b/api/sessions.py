# !!!
# WARNING: This file is autogenerated
# Only modify code within MANUAL() sections
# or your changes may be overwritten later!
# !!!

from __future__ import annotations

from typing import Any, Dict, Optional

from stytch.b2b.models.sessions import (
    AuthenticateResponse,
    ExchangeResponse,
    GetJWKSResponse,
    GetResponse,
    RevokeResponse,
)
from stytch.core.api_base import ApiBase
from stytch.core.http.client import AsyncClient, SyncClient


class Sessions:
    def __init__(
        self,
        api_base: ApiBase,
        sync_client: SyncClient,
        async_client: AsyncClient,
    ) -> None:
        self.api_base = api_base
        self.sync_client = sync_client
        self.async_client = async_client

    def get(
        self,
        organization_id: str,
        member_id: str,
    ) -> GetResponse:
        """Retrieves all active Sessions for a Member.

        Fields:
          - organization_id: Globally unique UUID that identifies a specific Organization. The `organization_id` is critical to perform operations on an Organization, so be sure to preserve this value.
          - member_id: Globally unique UUID that identifies a specific Member. The `member_id` is critical to perform operations on a Member, so be sure to preserve this value.
        """  # noqa
        data: Dict[str, Any] = {
            "organization_id": organization_id,
            "member_id": member_id,
        }

        url = self.api_base.url_for("/v1/b2b/sessions", data)
        res = self.sync_client.get(url, data)
        return GetResponse.from_json(res.response.status_code, res.json)

    async def get_async(
        self,
        organization_id: str,
        member_id: str,
    ) -> GetResponse:
        """Retrieves all active Sessions for a Member.

        Fields:
          - organization_id: Globally unique UUID that identifies a specific Organization. The `organization_id` is critical to perform operations on an Organization, so be sure to preserve this value.
          - member_id: Globally unique UUID that identifies a specific Member. The `member_id` is critical to perform operations on a Member, so be sure to preserve this value.
        """  # noqa
        data: Dict[str, Any] = {
            "organization_id": organization_id,
            "member_id": member_id,
        }

        url = self.api_base.url_for("/v1/b2b/sessions", data)
        res = await self.async_client.get(url, data)
        return GetResponse.from_json(res.response.status, res.json)

    def authenticate(
        self,
        session_token: Optional[str] = None,
        session_duration_minutes: Optional[int] = None,
        session_jwt: Optional[str] = None,
        session_custom_claims: Optional[Dict[str, Any]] = None,
    ) -> AuthenticateResponse:
        """Authenticates a Session and updates its lifetime by the specified `session_duration_minutes`. If the `session_duration_minutes` is not specified, a Session will not be extended. This endpoint requires either a `session_jwt` or `session_token` be included in the request. It will return an error if both are present.

        You may provide a JWT that needs to be refreshed and is expired according to its `exp` claim. A new JWT will be returned if both the signature and the underlying Session are still valid.

        Fields:
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
        data: Dict[str, Any] = {}
        if session_token is not None:
            data["session_token"] = session_token
        if session_duration_minutes is not None:
            data["session_duration_minutes"] = session_duration_minutes
        if session_jwt is not None:
            data["session_jwt"] = session_jwt
        if session_custom_claims is not None:
            data["session_custom_claims"] = session_custom_claims

        url = self.api_base.url_for("/v1/b2b/sessions/authenticate", data)
        res = self.sync_client.post(url, data)
        return AuthenticateResponse.from_json(res.response.status_code, res.json)

    async def authenticate_async(
        self,
        session_token: Optional[str] = None,
        session_duration_minutes: Optional[int] = None,
        session_jwt: Optional[str] = None,
        session_custom_claims: Optional[Dict[str, Any]] = None,
    ) -> AuthenticateResponse:
        """Authenticates a Session and updates its lifetime by the specified `session_duration_minutes`. If the `session_duration_minutes` is not specified, a Session will not be extended. This endpoint requires either a `session_jwt` or `session_token` be included in the request. It will return an error if both are present.

        You may provide a JWT that needs to be refreshed and is expired according to its `exp` claim. A new JWT will be returned if both the signature and the underlying Session are still valid.

        Fields:
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
        data: Dict[str, Any] = {}
        if session_token is not None:
            data["session_token"] = session_token
        if session_duration_minutes is not None:
            data["session_duration_minutes"] = session_duration_minutes
        if session_jwt is not None:
            data["session_jwt"] = session_jwt
        if session_custom_claims is not None:
            data["session_custom_claims"] = session_custom_claims

        url = self.api_base.url_for("/v1/b2b/sessions/authenticate", data)
        res = await self.async_client.post(url, data)
        return AuthenticateResponse.from_json(res.response.status, res.json)

    def revoke(
        self,
        member_session_id: Optional[str] = None,
        session_token: Optional[str] = None,
        session_jwt: Optional[str] = None,
        member_id: Optional[str] = None,
    ) -> RevokeResponse:
        """Revoke a Session and immediately invalidate all its tokens. To revoke a specific Session, pass either the `member_session_id`, `session_token`, or `session_jwt`. To revoke all Sessions for a Member, pass the `member_id`.

        Fields:
          - member_session_id: Globally unique UUID that identifies a specific Session in the Stytch API. The `member_session_id` is critical to perform operations on an Session, so be sure to preserve this value.
          - session_token: A secret token for a given Stytch Session.
          - session_jwt: The JSON Web Token (JWT) for a given Stytch Session.
          - member_id: Globally unique UUID that identifies a specific Member. The `member_id` is critical to perform operations on a Member, so be sure to preserve this value.
        """  # noqa
        data: Dict[str, Any] = {}
        if member_session_id is not None:
            data["member_session_id"] = member_session_id
        if session_token is not None:
            data["session_token"] = session_token
        if session_jwt is not None:
            data["session_jwt"] = session_jwt
        if member_id is not None:
            data["member_id"] = member_id

        url = self.api_base.url_for("/v1/b2b/sessions/revoke", data)
        res = self.sync_client.post(url, data)
        return RevokeResponse.from_json(res.response.status_code, res.json)

    async def revoke_async(
        self,
        member_session_id: Optional[str] = None,
        session_token: Optional[str] = None,
        session_jwt: Optional[str] = None,
        member_id: Optional[str] = None,
    ) -> RevokeResponse:
        """Revoke a Session and immediately invalidate all its tokens. To revoke a specific Session, pass either the `member_session_id`, `session_token`, or `session_jwt`. To revoke all Sessions for a Member, pass the `member_id`.

        Fields:
          - member_session_id: Globally unique UUID that identifies a specific Session in the Stytch API. The `member_session_id` is critical to perform operations on an Session, so be sure to preserve this value.
          - session_token: A secret token for a given Stytch Session.
          - session_jwt: The JSON Web Token (JWT) for a given Stytch Session.
          - member_id: Globally unique UUID that identifies a specific Member. The `member_id` is critical to perform operations on a Member, so be sure to preserve this value.
        """  # noqa
        data: Dict[str, Any] = {}
        if member_session_id is not None:
            data["member_session_id"] = member_session_id
        if session_token is not None:
            data["session_token"] = session_token
        if session_jwt is not None:
            data["session_jwt"] = session_jwt
        if member_id is not None:
            data["member_id"] = member_id

        url = self.api_base.url_for("/v1/b2b/sessions/revoke", data)
        res = await self.async_client.post(url, data)
        return RevokeResponse.from_json(res.response.status, res.json)

    def exchange(
        self,
        organization_id: str,
        session_token: Optional[str] = None,
        session_jwt: Optional[str] = None,
        session_duration_minutes: Optional[int] = None,
        session_custom_claims: Optional[Dict[str, Any]] = None,
    ) -> ExchangeResponse:
        """Use this endpoint to exchange a Member's existing session for another session in a different Organization. This can be used to accept an invite, but not to create a new member via domain matching.

        To create a new member via domain matching, use the [Exchange Intermediate Session](https://stytch.com/docs/b2b/api/exchange-intermediate-session) flow instead.

        Fields:
          - organization_id: Globally unique UUID that identifies a specific Organization. The `organization_id` is critical to perform operations on an Organization, so be sure to preserve this value.
          - session_token: The `session_token` belonging to the member that you wish to associate the email with.
          - session_jwt: The `session_jwt` belonging to the member that you wish to associate the email with.
          - session_duration_minutes: Set the session lifetime to be this many minutes from now. This will start a new session if one doesn't already exist,
          returning both an opaque `session_token` and `session_jwt` for this session. Remember that the `session_jwt` will have a fixed lifetime of
          five minutes regardless of the underlying session duration, and will need to be refreshed over time.

          This value must be a minimum of 5 and a maximum of 527040 minutes (366 days).

          If a `session_token` or `session_jwt` is provided then a successful authentication will continue to extend the session this many minutes.

          If the `session_duration_minutes` parameter is not specified, a Stytch session will be created with a 60 minute duration. If you don't want
          to use the Stytch session product, you can ignore the session fields in the response.
          - session_custom_claims: Add a custom claims map to the Session being authenticated. Claims are only created if a Session is initialized by providing a value in
          `session_duration_minutes`. Claims will be included on the Session object and in the JWT. To update a key in an existing Session, supply a new value. To
          delete a key, supply a null value. Custom claims made with reserved claims (`iss`, `sub`, `aud`, `exp`, `nbf`, `iat`, `jti`) will be ignored.
          Total custom claims size cannot exceed four kilobytes.
        """  # noqa
        data: Dict[str, Any] = {
            "organization_id": organization_id,
        }
        if session_token is not None:
            data["session_token"] = session_token
        if session_jwt is not None:
            data["session_jwt"] = session_jwt
        if session_duration_minutes is not None:
            data["session_duration_minutes"] = session_duration_minutes
        if session_custom_claims is not None:
            data["session_custom_claims"] = session_custom_claims

        url = self.api_base.url_for("/v1/b2b/sessions/exchange", data)
        res = self.sync_client.post(url, data)
        return ExchangeResponse.from_json(res.response.status_code, res.json)

    async def exchange_async(
        self,
        organization_id: str,
        session_token: Optional[str] = None,
        session_jwt: Optional[str] = None,
        session_duration_minutes: Optional[int] = None,
        session_custom_claims: Optional[Dict[str, Any]] = None,
    ) -> ExchangeResponse:
        """Use this endpoint to exchange a Member's existing session for another session in a different Organization. This can be used to accept an invite, but not to create a new member via domain matching.

        To create a new member via domain matching, use the [Exchange Intermediate Session](https://stytch.com/docs/b2b/api/exchange-intermediate-session) flow instead.

        Fields:
          - organization_id: Globally unique UUID that identifies a specific Organization. The `organization_id` is critical to perform operations on an Organization, so be sure to preserve this value.
          - session_token: The `session_token` belonging to the member that you wish to associate the email with.
          - session_jwt: The `session_jwt` belonging to the member that you wish to associate the email with.
          - session_duration_minutes: Set the session lifetime to be this many minutes from now. This will start a new session if one doesn't already exist,
          returning both an opaque `session_token` and `session_jwt` for this session. Remember that the `session_jwt` will have a fixed lifetime of
          five minutes regardless of the underlying session duration, and will need to be refreshed over time.

          This value must be a minimum of 5 and a maximum of 527040 minutes (366 days).

          If a `session_token` or `session_jwt` is provided then a successful authentication will continue to extend the session this many minutes.

          If the `session_duration_minutes` parameter is not specified, a Stytch session will be created with a 60 minute duration. If you don't want
          to use the Stytch session product, you can ignore the session fields in the response.
          - session_custom_claims: Add a custom claims map to the Session being authenticated. Claims are only created if a Session is initialized by providing a value in
          `session_duration_minutes`. Claims will be included on the Session object and in the JWT. To update a key in an existing Session, supply a new value. To
          delete a key, supply a null value. Custom claims made with reserved claims (`iss`, `sub`, `aud`, `exp`, `nbf`, `iat`, `jti`) will be ignored.
          Total custom claims size cannot exceed four kilobytes.
        """  # noqa
        data: Dict[str, Any] = {
            "organization_id": organization_id,
        }
        if session_token is not None:
            data["session_token"] = session_token
        if session_jwt is not None:
            data["session_jwt"] = session_jwt
        if session_duration_minutes is not None:
            data["session_duration_minutes"] = session_duration_minutes
        if session_custom_claims is not None:
            data["session_custom_claims"] = session_custom_claims

        url = self.api_base.url_for("/v1/b2b/sessions/exchange", data)
        res = await self.async_client.post(url, data)
        return ExchangeResponse.from_json(res.response.status, res.json)

    def get_jwks(
        self,
        project_id: str,
    ) -> GetJWKSResponse:
        """Get the JSON Web Key Set (JWKS) for a project.

        Fields:
          - project_id: The `project_id` to get the JWKS for.
        """  # noqa
        data: Dict[str, Any] = {
            "project_id": project_id,
        }

        url = self.api_base.url_for("/v1/b2b/sessions/jwks/{project_id}", data)
        res = self.sync_client.get(url, data)
        return GetJWKSResponse.from_json(res.response.status_code, res.json)

    async def get_jwks_async(
        self,
        project_id: str,
    ) -> GetJWKSResponse:
        """Get the JSON Web Key Set (JWKS) for a project.

        Fields:
          - project_id: The `project_id` to get the JWKS for.
        """  # noqa
        data: Dict[str, Any] = {
            "project_id": project_id,
        }

        url = self.api_base.url_for("/v1/b2b/sessions/jwks/{project_id}", data)
        res = await self.async_client.get(url, data)
        return GetJWKSResponse.from_json(res.response.status, res.json)
