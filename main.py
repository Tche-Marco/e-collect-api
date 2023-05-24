import uvicorn
from fastapi import FastAPI

from app.api.routes import api_router
from app.database import Base, engine, SessionLocal
from app.models.ewaste import TrashType


app = FastAPI()


def create_tables():
    Base.metadata.create_all(bind=engine)


def startup():
    create_tables()


app.add_event_handler("startup", startup)

app.include_router(api_router, prefix="")


if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
