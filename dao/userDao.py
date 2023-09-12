from sqlalchemy.orm import Session
from db.models.users import User

from db.pymodels.users import User_In


def create_user(db: Session, user: User_In):
    db_user = User(**user.model_dump())
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def get_user(user_id: int, db: Session):
    return db.query(User).filter(User.id == user_id).first()


def get_user_by_email(email: str, db: Session):
    return db.query(User).filter(User.email == email).first()


def get_users(db: Session):
    return db.query(User).all()


def update_user(db: Session, user_data):
    updated_user = db.merge(user_data)
    db.commit()
    db.refresh(updated_user)
    return updated_user


def delete_user(db: Session, user_id: int):
    deleted_user = db.query(User).filter(User.id == user_id).delete()
    db.commit()
    return deleted_user
