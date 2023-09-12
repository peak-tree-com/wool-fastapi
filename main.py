from fastapi import FastAPI
import uvicorn

from db.dbConfig import engine
from db.models import users

from routers import users as apiUsers

# drop tables
users.Base.metadata.drop_all(engine)
# create tables
users.Base.metadata.create_all(bind=engine)

app = FastAPI(
    openapi_url="/api/v1/openapi.json",
    title="BusRouteApp",
    description="App for booking bus tickets",
    version="0.0.1",
    terms_of_service="http://peak-tree.com/terms_and_conditions",
    contact={
        "name": "Peak Tree",
        "email": "krithick@peak-tree.com",
    },
    license_info={
        "name": "MIT",
    },
)

app.include_router(apiUsers.router)


def start():
    """Launched with `poetry run start` at root level"""
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
