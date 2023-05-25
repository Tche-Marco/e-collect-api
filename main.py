import uvicorn
from fastapi import FastAPI

from app.core.establishment.endpoints import router as establishment_router
from app.core.trash_type.endpoints import router as trash_type_router
from app.core.disposal.endpoints import router as disposals_router
from app.core.offer.endpoints import router as offers_router
from app.core.user.endpoints import router as user_router
from app.core.database import Base, engine


app = FastAPI()


def create_tables():
    Base.metadata.create_all(bind=engine)


def startup():
    create_tables()


app.add_event_handler("startup", startup)


app.include_router(
    user_router,
    prefix="/users",
    tags=["Usuários"],
)
app.include_router(
    establishment_router,
    prefix="/establishments",
    tags=["Estabelecimentos"],
)
app.include_router(
    disposals_router,
    prefix="/disposals",
    tags=["Descartes"],
)
app.include_router(
    trash_type_router,
    prefix="/trash_types",
    tags=["Tipos de lixo"],
)
app.include_router(
    offers_router,
    prefix="/offers",
    tags=["Ofertas"],
)


if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
