from datetime import datetime
from enum import Enum
from typing import Optional
from pydantic import BaseModel

from db.models.users import Role


class UserBase(BaseModel):
    email: Optional[str] = None
    role: Optional[Role] = None


class User_In(UserBase):
    password: Optional[str] = None


class User_Out(UserBase):
    id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True
