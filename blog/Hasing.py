
from passlib.context import CryptContext

pwd_cxt = CryptContext(schemes=['bcrypt'], deprecated='auto')

class Hash():

    @staticmethod # this is optional.
    def bcrypt(password: str):
        return pwd_cxt.hash(password)

    def verify(hashed_password, plain_password):
        # first give plain password, and then verify password in function
        return pwd_cxt.verify(plain_password, hashed_password)
        