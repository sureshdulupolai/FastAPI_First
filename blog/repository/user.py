from sqlalchemy.orm import Session
from blog import model, schemas
from blog.Hasing import Hash
from fastapi import HTTPException, status

def create_new_user(request: schemas.User, db: Session):
    # hasedPassword = pwd_cxt.hash(request.password)
    new_user = model.User(name=request.name, email=request.email, password=Hash.bcrypt(request.password))
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


def get_user_detail(user_id: int, db: Session):
    user = db.query(model.User).filter(model.User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Blog with the id {user_id} is not available')
    return user
