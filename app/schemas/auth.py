from pydantic import BaseModel, ConfigDict
from typing import Optional

class LoginRequest(BaseModel):
    username: str
    password: str
    device_id: Optional[str] = None

class TokenResponse(BaseModel):
    access_token: Optional[str] = None
    token_type: str = "bearer"
    mfa_required: bool = False
    mfa_token: Optional[str] = None
    expires_in: Optional[int] = None
    user: Optional[dict] = None

    model_config = ConfigDict(from_attributes=True)

class MfaVerifyRequest(BaseModel):
    mfa_token: str
    totp_code: Optional[str] = None
    recovery_code: Optional[str] = None
    device_id: Optional[str] = None

class MfaSetupRequest(BaseModel):
    password: str

class MfaSetupResponse(BaseModel):
    otp_auth_url: str
    manual_secret: str
    recovery_codes: list[str]

class MfaConfirmRequest(BaseModel):
    totp_code: str