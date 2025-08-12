from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from blog.token import verify_token

# tokenUrl -> mean the router.auth -> /login
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")

def get_current_user(token: str = Depends(oauth2_scheme)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )

    return verify_token(token, credentials_exception)