from sqlalchemy.orm import Session
from db.models.users import User
from middleware.auth import pwd_context
from db.pymodels.users import User_In


def create_user(db: Session, user: User_In):
    db_user = User(
        email=user.email,
        hashed_password=pwd_context.hash(user.password),
        role=user.role,
        username=user.username,
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def get_user_by_id(user_id: int, db: Session):
    return db.query(User).filter(User.id == user_id).first()


def get_user_by_email(email: str, db: Session):
    user = db.query(User).filter(User.email == email).first()
    return user


def get_user_by_username(username: str, db: Session):
    user = db.query(User).filter(User.username == username).first()
    return user


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
