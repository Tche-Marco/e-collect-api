import uvicorn
from fastapi import FastAPI

from app.database import Base, engine
from app.api.routes import api_router
from app.core.user.endpoints import router as user_router


app = FastAPI()


def create_tables():
    Base.metadata.create_all(bind=engine)


def startup():
    create_tables()


app.add_event_handler("startup", startup)

app.include_router(api_router, prefix="")
app.include_router(user_router, prefix="/users")


if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
