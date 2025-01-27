# !!!
# WARNING: This file is autogenerated
# Only modify code within MANUAL() sections
# or your changes may be overwritten later!
# !!!

from __future__ import annotations

import datetime
from typing import Any, Dict, List

import pydantic

from stytch.b2b.models.organizations import Member, Organization
from stytch.consumer.models.sessions import JWK, AuthenticationFactor
from stytch.core.response_base import ResponseBase


class MemberSession(pydantic.BaseModel):
    """
    Fields:
      - member_session_id: Globally unique UUID that identifies a specific Session.
      - member_id: Globally unique UUID that identifies a specific Member.
      - started_at: The timestamp when the Session was created. Values conform to the RFC 3339 standard and are expressed in UTC, e.g. `2021-12-29T12:33:09Z`.
      - last_accessed_at: The timestamp when the Session was last accessed. Values conform to the RFC 3339 standard and are expressed in UTC, e.g. `2021-12-29T12:33:09Z`.
      - expires_at: The timestamp when the Session expires. Values conform to the RFC 3339 standard and are expressed in UTC, e.g. `2021-12-29T12:33:09Z`.
      - authentication_factors: An array of different authentication factors that have initiated a Session.
      - custom_claims: The custom claims map for a Session. Claims can be added to a session during a Sessions authenticate call.
      - organization_id: Globally unique UUID that identifies a specific Organization. The `organization_id` is critical to perform operations on an Organization, so be sure to preserve this value.
    """  # noqa

    member_session_id: str
    member_id: str
    started_at: datetime.datetime
    last_accessed_at: datetime.datetime
    expires_at: datetime.datetime
    authentication_factors: List[AuthenticationFactor]
    custom_claims: Dict[str, Any]
    organization_id: str


class AuthenticateResponse(ResponseBase):
    """Response type for `Sessions.authenticate`.
    Fields:
      - member_session: The [Session object](https://stytch.com/docs/b2b/api/session-object).
      - session_token: A secret token for a given Stytch Session.
      - session_jwt: The JSON Web Token (JWT) for a given Stytch Session.
      - member: The [Member object](https://stytch.com/docs/b2b/api/member-object).
      - organization: The [Organization object](https://stytch.com/docs/b2b/api/organization-object).
    """  # noqa

    member_session: MemberSession
    session_token: str
    session_jwt: str
    member: Member
    organization: Organization


class ExchangeResponse(ResponseBase):
    """Response type for `Sessions.exchange`.
    Fields:
      - member_id: Globally unique UUID that identifies a specific Member.
      - member_session: The [Session object](https://stytch.com/docs/b2b/api/session-object).
      - session_token: A secret token for a given Stytch Session.
      - session_jwt: The JSON Web Token (JWT) for a given Stytch Session.
      - member: The [Member object](https://stytch.com/docs/b2b/api/member-object).
      - organization: The [Organization object](https://stytch.com/docs/b2b/api/organization-object).
    """  # noqa

    member_id: str
    member_session: MemberSession
    session_token: str
    session_jwt: str
    member: Member
    organization: Organization


class GetJWKSResponse(ResponseBase):
    """Response type for `Sessions.get_jwks`.
    Fields:
      - keys: The JWK
    """  # noqa

    keys: List[JWK]


class GetResponse(ResponseBase):
    """Response type for `Sessions.get`.
    Fields:
      - member_sessions: An array of [Session objects](https://stytch.com/docs/b2b/api/session-object).
    """  # noqa

    member_sessions: List[MemberSession]


class RevokeResponse(ResponseBase):
    """Response type for `Sessions.revoke`.
    Fields:
    """  # noqa
