# !!!
# WARNING: This file is autogenerated
# Only modify code within MANUAL() sections
# or your changes may be overwritten later!
# !!!

from typing import Any, Dict, List, Optional

from stytch.b2b.models.discovery_organizations import CreateResponse, ListResponse
from stytch.core.api_base import ApiBase
from stytch.core.http.client import AsyncClient, SyncClient


class Organizations:
    def __init__(
        self,
        api_base: ApiBase,
        sync_client: SyncClient,
        async_client: AsyncClient,
    ) -> None:
        self.api_base = api_base
        self.sync_client = sync_client
        self.async_client = async_client

    @property
    def sub_url(self) -> str:
        return "discovery/organizations"

    def list(
        self,
        intermediate_session_token: Optional[str] = None,
        session_token: Optional[str] = None,
        session_jwt: Optional[str] = None,
    ) -> ListResponse:
        """List all possible organization relationships connected to a Member Session or Intermediate Session.

        When a Member Session is passed in, relationships with a type of `active_member`, `pending_member`, or `invited_member` will be returned, and any membership can be assumed by calling the [Exchange Session](https://stytch.com/docs/b2b/api/exchange-session) endpoint.

        When an Intermediate Session is passed in, all relationship types - `active_member`, `pending_member`, `invited_member`, and `eligible_to_join_by_email_domain` - will be returned, and any membership can be assumed by calling the [Exchange Intermediate Session](https://stytch.com/docs/b2b/api/exchange-intermediate-session) endpoint.

        This endpoint requires either an `intermediate_session_token`, `session_jwt` or `session_token` be included in the request. It will return an error if multiple are present.

        This operation does not consume the Intermediate Session or Session Token passed in.

        Parameters:

        - `intermediate_session_token`: The intermediate session token.

        - `session_token`: A secret token for a given Stytch Session.

        - `session_jwt`: The JSON Web Token (JWT) for a given Stytch Session.
        """  # noqa

        payload: Dict[str, Any] = {}

        if intermediate_session_token is not None:
            payload["intermediate_session_token"] = intermediate_session_token
        if session_token is not None:
            payload["session_token"] = session_token
        if session_jwt is not None:
            payload["session_jwt"] = session_jwt

        url = self.api_base.route_with_sub_url(self.sub_url, None)

        res = self.sync_client.post(url, json=payload)
        return ListResponse.from_json(res.response.status_code, res.json)

    async def list_async(
        self,
        intermediate_session_token: Optional[str] = None,
        session_token: Optional[str] = None,
        session_jwt: Optional[str] = None,
    ) -> ListResponse:
        """List all possible organization relationships connected to a Member Session or Intermediate Session.

        When a Member Session is passed in, relationships with a type of `active_member`, `pending_member`, or `invited_member` will be returned, and any membership can be assumed by calling the [Exchange Session](https://stytch.com/docs/b2b/api/exchange-session) endpoint.

        When an Intermediate Session is passed in, all relationship types - `active_member`, `pending_member`, `invited_member`, and `eligible_to_join_by_email_domain` - will be returned, and any membership can be assumed by calling the [Exchange Intermediate Session](https://stytch.com/docs/b2b/api/exchange-intermediate-session) endpoint.

        This endpoint requires either an `intermediate_session_token`, `session_jwt` or `session_token` be included in the request. It will return an error if multiple are present.

        This operation does not consume the Intermediate Session or Session Token passed in.

        Parameters:

        - `intermediate_session_token`: The intermediate session token.

        - `session_token`: A secret token for a given Stytch Session.

        - `session_jwt`: The JSON Web Token (JWT) for a given Stytch Session.
        """  # noqa

        payload: Dict[str, Any] = {}

        if intermediate_session_token is not None:
            payload["intermediate_session_token"] = intermediate_session_token
        if session_token is not None:
            payload["session_token"] = session_token
        if session_jwt is not None:
            payload["session_jwt"] = session_jwt

        url = self.api_base.route_with_sub_url(self.sub_url, None)

        res = await self.async_client.post(url, json=payload)
        return ListResponse.from_json(res.response.status, res.json)

    def create(
        self,
        intermediate_session_token: str,
        organization_name: str,
        organization_slug: str,
        session_duration_minutes: Optional[int] = None,
        session_custom_claims: Optional[Dict[str, Any]] = None,
        organization_logo_url: Optional[str] = None,
        trusted_metadata: Optional[Dict[str, Any]] = None,
        email_jit_provisioning: Optional[str] = None,
        email_invites: Optional[str] = None,
        email_allowed_domains: Optional[List[str]] = None,
        sso_jit_provisioning: Optional[str] = None,
        auth_methods: Optional[str] = None,
        allowed_auth_methods: Optional[List[str]] = None,
    ) -> CreateResponse:
        """If an end user does not want to join any already-existing organization, or has no possible organizations to join, this endpoint can be used to create a new Organization and Member.

        This operation consumes the Intermediate Session.

        This endpoint can also be used to start an initial session for the newly created member and organization.

        Parameters:

        - `intermediate_session_token`: The Intermediate Session Token to consume to create the new Organization and Member.

        - `session_duration_minutes`: Set the session lifetime to be this many minutes from now. This will start a new session if one doesn't already exist, returning both an opaque `session_token` and `session_jwt` for this session. Remember that the `session_jwt` will have a fixed lifetime of five minutes regardless of the underlying session duration, and will need to be refreshed over time.
          - This value must be a minimum of 5 and a maximum of 527040 minutes (366 days).
          - If a `session_token` or `session_jwt` is provided then a successful authentication will continue to extend the session this many minutes.
          - If the `session_duration_minutes` parameter is not specified, a Stytch session will be created with a 60 minute duration. If you don't want to use the Stytch session product, you can ignore the session fields in the response.

        - `session_custom_claims`: Add a custom claims map to the session being authenticated. Claims will be included on the session object and in the JWT. To update a key in an existing session, supply a new value. To delete a key, supply a null value.

        - `organization_name`: The name of the Organization.

        - `organization_slug`: The unique URL slug of the Organization.

        - `organization_logo_url`: The image URL of the Organization’s logo.

        - `trusted_metadata`: An arbitrary JSON object for storing application-specific data.

        - `email_jit_provisioning`: The setting that controls the JIT provisioning of new Members when authenticating via email. The accepted values are:

            - RESTRICTED – only new Members with verified emails that comply with `email_allowed_domains` can be provisioned upon authentication.
            - NOT_ALLOWED – disable JIT provisioning.

        - `email_invites`: The setting that controls how a new Member can be invited to an organization by email. The accepted values are:

            - ALL_ALLOWED – any new Member can be invited to join
            - RESTRICTED – only new Members with verified emails that comply with `email_allowed_domains` can be invited
            - NOT_ALLOWED – disable invites

        - `email_allowed_domains`: An array of email domains that allow invitations or JIT provisioning for new Members. This list is enforced when either email_invites or email_jit_provisioning is set to RESTRICTED.

        - `sso_jit_provisioning`: The setting that controls the JIT provisioning of Members when authenticating via SSO. The accepted values are:
            - ALL_ALLOWED – any new Member can be provisioned upon authentication
            - RESTRICTED – only new Members with SSO logins that comply with `sso_jit_provisioning_allowed_connections` can be provisioned upon authentication
            - NOT_ALLOWED – disable JIT provisioning

        - `auth_methods`: The setting that controls which authentication methods can be used by Members of an Organization. The accepted values are:
            - ALL_ALLOWED – the default setting which allows all authentication methods to be used.
            - RESTRICTED - only methods that comply with `allowed_auth_methods` can be used for authentication. This setting does not apply to Members with `is_breakglass` set to `true`.

        - `allowed_auth_methods`: An array of allowed authentication methods. This list is enforced when auth_methods is set to RESTRICTED. The list's accepted values are: `sso`, `magic_link`, and `password`.
        """  # noqa

        payload: Dict[str, Any] = {
            "intermediate_session_token": intermediate_session_token,
            "organization_name": organization_name,
            "organization_slug": organization_slug,
        }

        if session_duration_minutes is not None:
            payload["session_duration_minutes"] = session_duration_minutes
        if session_custom_claims is not None:
            payload["session_custom_claims"] = session_custom_claims
        if organization_logo_url is not None:
            payload["organization_logo_url"] = organization_logo_url
        if trusted_metadata is not None:
            payload["trusted_metadata"] = trusted_metadata
        if email_jit_provisioning is not None:
            payload["email_jit_provisioning"] = email_jit_provisioning
        if email_invites is not None:
            payload["email_invites"] = email_invites
        if email_allowed_domains is not None:
            payload["email_allowed_domains"] = email_allowed_domains
        if sso_jit_provisioning is not None:
            payload["sso_jit_provisioning"] = sso_jit_provisioning
        if auth_methods is not None:
            payload["auth_methods"] = auth_methods
        if allowed_auth_methods is not None:
            payload["allowed_auth_methods"] = allowed_auth_methods

        url = self.api_base.route_with_sub_url(self.sub_url, "create")

        res = self.sync_client.post(url, json=payload)
        return CreateResponse.from_json(res.response.status_code, res.json)

    async def create_async(
        self,
        intermediate_session_token: str,
        organization_name: str,
        organization_slug: str,
        session_duration_minutes: Optional[int] = None,
        session_custom_claims: Optional[Dict[str, Any]] = None,
        organization_logo_url: Optional[str] = None,
        trusted_metadata: Optional[Dict[str, Any]] = None,
        email_jit_provisioning: Optional[str] = None,
        email_invites: Optional[str] = None,
        email_allowed_domains: Optional[List[str]] = None,
        sso_jit_provisioning: Optional[str] = None,
        auth_methods: Optional[str] = None,
        allowed_auth_methods: Optional[List[str]] = None,
    ) -> CreateResponse:
        """If an end user does not want to join any already-existing organization, or has no possible organizations to join, this endpoint can be used to create a new Organization and Member.

        This operation consumes the Intermediate Session.

        This endpoint can also be used to start an initial session for the newly created member and organization.

        Parameters:

        - `intermediate_session_token`: The Intermediate Session Token to consume to create the new Organization and Member.

        - `session_duration_minutes`: Set the session lifetime to be this many minutes from now. This will start a new session if one doesn't already exist, returning both an opaque `session_token` and `session_jwt` for this session. Remember that the `session_jwt` will have a fixed lifetime of five minutes regardless of the underlying session duration, and will need to be refreshed over time.
          - This value must be a minimum of 5 and a maximum of 527040 minutes (366 days).
          - If a `session_token` or `session_jwt` is provided then a successful authentication will continue to extend the session this many minutes.
          - If the `session_duration_minutes` parameter is not specified, a Stytch session will be created with a 60 minute duration. If you don't want to use the Stytch session product, you can ignore the session fields in the response.

        - `session_custom_claims`: Add a custom claims map to the session being authenticated. Claims will be included on the session object and in the JWT. To update a key in an existing session, supply a new value. To delete a key, supply a null value.

        - `organization_name`: The name of the Organization.

        - `organization_slug`: The unique URL slug of the Organization.

        - `organization_logo_url`: The image URL of the Organization’s logo.

        - `trusted_metadata`: An arbitrary JSON object for storing application-specific data.

        - `email_jit_provisioning`: The setting that controls the JIT provisioning of new Members when authenticating via email. The accepted values are:

            - RESTRICTED – only new Members with verified emails that comply with `email_allowed_domains` can be provisioned upon authentication.
            - NOT_ALLOWED – disable JIT provisioning.

        - `email_invites`: The setting that controls how a new Member can be invited to an organization by email. The accepted values are:

            - ALL_ALLOWED – any new Member can be invited to join
            - RESTRICTED – only new Members with verified emails that comply with `email_allowed_domains` can be invited
            - NOT_ALLOWED – disable invites

        - `email_allowed_domains`: An array of email domains that allow invitations or JIT provisioning for new Members. This list is enforced when either email_invites or email_jit_provisioning is set to RESTRICTED.

        - `sso_jit_provisioning`: The setting that controls the JIT provisioning of Members when authenticating via SSO. The accepted values are:
            - ALL_ALLOWED – any new Member can be provisioned upon authentication
            - RESTRICTED – only new Members with SSO logins that comply with `sso_jit_provisioning_allowed_connections` can be provisioned upon authentication
            - NOT_ALLOWED – disable JIT provisioning

        - `auth_methods`: The setting that controls which authentication methods can be used by Members of an Organization. The accepted values are:
            - ALL_ALLOWED – the default setting which allows all authentication methods to be used.
            - RESTRICTED - only methods that comply with `allowed_auth_methods` can be used for authentication. This setting does not apply to Members with `is_breakglass` set to `true`.

        - `allowed_auth_methods`: An array of allowed authentication methods. This list is enforced when auth_methods is set to RESTRICTED. The list's accepted values are: `sso`, `magic_link`, and `password`.
        """  # noqa

        payload: Dict[str, Any] = {
            "intermediate_session_token": intermediate_session_token,
            "organization_name": organization_name,
            "organization_slug": organization_slug,
        }

        if session_duration_minutes is not None:
            payload["session_duration_minutes"] = session_duration_minutes
        if session_custom_claims is not None:
            payload["session_custom_claims"] = session_custom_claims
        if organization_logo_url is not None:
            payload["organization_logo_url"] = organization_logo_url
        if trusted_metadata is not None:
            payload["trusted_metadata"] = trusted_metadata
        if email_jit_provisioning is not None:
            payload["email_jit_provisioning"] = email_jit_provisioning
        if email_invites is not None:
            payload["email_invites"] = email_invites
        if email_allowed_domains is not None:
            payload["email_allowed_domains"] = email_allowed_domains
        if sso_jit_provisioning is not None:
            payload["sso_jit_provisioning"] = sso_jit_provisioning
        if auth_methods is not None:
            payload["auth_methods"] = auth_methods
        if allowed_auth_methods is not None:
            payload["allowed_auth_methods"] = allowed_auth_methods

        url = self.api_base.route_with_sub_url(self.sub_url, "create")

        res = await self.async_client.post(url, json=payload)
        return CreateResponse.from_json(res.response.status, res.json)
