from enum import Enum
from sqlalchemy import (
    Boolean,
    Column,
    ForeignKey,
    Integer,
    String,
    Enum as SQLAlchemyEnum,
    Text,
)

from db.models.mixins import Timestamp
from ..dbConfig import Base
from sqlalchemy_utils import EmailType
from sqlalchemy.orm import relationship


class Sex(Enum):
    female = 0
    male = 1
    others = 2


class Role(Enum):
    guest = 0
    buyer = 1
    seller = 2


class User(Timestamp, Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(EmailType, nullable=False)
    hashed_password = Column(String)
    role = Column(SQLAlchemyEnum(Role))
    is_active = Column(Boolean, default=True)
    username = Column(String, nullable=False, unique=True)

    profile = relationship("Profile", back_populates="owner", uselist=False)


class Profile(Timestamp, Base):
    __tablename__ = "profiles"

    id = Column(Integer, primary_key=True, index=True)
    display_profile = Column(String)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=True)
    gender = Column(SQLAlchemyEnum(Sex))
    bio = Column(Text, nullable=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)

    owner = relationship("User", back_populates="profile")
