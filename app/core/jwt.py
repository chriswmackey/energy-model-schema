import jwt
from fastapi import Security

from .security import security_scheme
from app.models.security import TokenPayload

def get_user_info(token: str = Security(security_scheme)):
        payload = jwt.decode(token.credentials, verify=False)
        token_data = TokenPayload(**payload)
        return token_data
