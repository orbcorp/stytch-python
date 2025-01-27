# !!!
# WARNING: This file is autogenerated
# Only modify code within MANUAL() sections
# or your changes may be overwritten later!
# !!!

from __future__ import annotations

from stytch.b2b.models.organizations import Member, Organization
from stytch.b2b.models.sessions import MemberSession
from stytch.core.response_base import ResponseBase


class AuthenticateResponse(ResponseBase):
    """Response type for `MagicLinks.authenticate`.
    Fields:
      - member_id: Globally unique UUID that identifies a specific Member.
      - method_id: The email or device involved in the authentication.
      - reset_sessions: Indicates if all Sessions linked to the Member need to be reset. You should check this field if you aren't using
        Stytch's Session product. If you are using Stytch's Session product, we revoke the Member’s other Sessions for you.
      - organization_id: Globally unique UUID that identifies a specific Organization. The `organization_id` is critical to perform operations on an Organization, so be sure to preserve this value.
      - member: The [Member object](https://stytch.com/docs/b2b/api/member-object).
      - session_token: A secret token for a given Stytch Session.
      - session_jwt: The JSON Web Token (JWT) for a given Stytch Session.
      - member_session: The [Session object](https://stytch.com/docs/b2b/api/session-object).
      - organization: The [Organization object](https://stytch.com/docs/b2b/api/organization-object).
    """  # noqa

    member_id: str
    method_id: str
    reset_sessions: bool
    organization_id: str
    member: Member
    session_token: str
    session_jwt: str
    member_session: MemberSession
    organization: Organization
