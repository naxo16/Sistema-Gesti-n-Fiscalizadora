from pydantic import BaseModel

class LoginRequest(BaseModel):
    imei_hash: str

class Token(BaseModel):
    access_token: str
    token_type: str = "bearer"