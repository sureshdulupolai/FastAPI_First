from fastapi import APIRouter, Depends, HTTPException, status
from blog import schemas, database, model, token
from sqlalchemy.orm import Session
from blog.Hasing import Hash
from fastapi.security import OAuth2PasswordRequestForm

auth_router = APIRouter(
    tags=['Authentication']
)


# username -> gmail here
@auth_router.post('/login')
def login(request: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(database.get_db)):
    user = db.query(model.User).filter(model.User.email == request.username).first()

    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Invalid Credentials In Gmail')

    if not Hash.verify(user.password, request.password):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Invalid Credentials In Password')

    # Generate a JWT token and return it.
    access_token = token.create_access_token(
        data={"sub": user.email}
    )
    return {"access_token" : access_token, "token_type" : "bearer"}