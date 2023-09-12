from fastapi import APIRouter, Depends, HTTPException
from db.dbConfig import get_db
from db.pymodels.users import User_In, User_Out
from sqlalchemy.orm import Session
import dao.userDao as userCrud

router = APIRouter(
    prefix="/api/users",
    tags=["Users"],
    responses={404: {"description": "Not found"}},
)


@router.post("/createUser", response_model=User_Out, status_code=201)
async def createUser(user: User_In, db: Session = Depends(get_db)):
    db_user = userCrud.get_user_by_email(email=user.email, db=db)
    if db_user:
        raise HTTPException(status_code=400, detail="email already exists")

    return userCrud.create_user(db=db, user=user)


@router.get("/getUserById/{user_id}", status_code=200)
async def getUserById(user_id: int, db: Session = Depends(get_db)):
    db_user = userCrud.get_user(user_id=user_id, db=db)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user


@router.get("/getAllUsers", status_code=200)
async def getAllUsers(db: Session = Depends(get_db)):
    users = userCrud.get_users(db)
    if users is None:
        raise HTTPException(status_code=404, detail="No Users Found")
    return users


@router.patch("/UpdateUserById/{user_id}", status_code=200)
async def UpdateUserById(
    user_id: int, user_req: User_In, db: Session = Depends(get_db)
):
    user = userCrud.get_user(user_id=user_id, db=db)  # get object

    if user is None:  # check if user exist
        raise HTTPException(status_code=404, detail="User not found")

    user_data = user_req.model_dump(exclude_unset=True)  # excluding null key
    if "name" in user_data:
        user.name = user_data["name"]

    if "age" in user_data:
        user.age = user_data["age"]

    if "sex" in user_data:
        user.sex = user_data["sex"]
    return userCrud.update_user(db, user)


@router.delete("/deleteUserById/{user_id}")
async def deleteUserById(user_id: int, db: Session = Depends(get_db)):
    db_user = userCrud.get_user(user_id=user_id, db=db)  # getting object
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return userCrud.delete_user(db=db, user_id=user_id)  # deleting the retrieved
