from sqlalchemy.orm import Session
from models import User
from schemas import UserCreate, UserResponse

def create_user(user: UserCreate, hashed_password: str, db: Session):
    db_user = User(username=user.username, email=user.email, password=hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return UserResponse.from_orm(db_user)

def get_user(user_id: int, db: Session):
    return db.query(User).get(user_id)
