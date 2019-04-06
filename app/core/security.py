from fastapi.security import HTTPBearer

security_scheme = HTTPBearer(bearerFormat='jwt', scheme_name='JWT')
