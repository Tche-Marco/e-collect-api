from fastapi import APIRouter

from app.establishment.endpoints import router as establishment_router
from app.trash_type.endpoints import router as trash_type_router
from app.disposal.endpoints import router as disposals_router
from app.offer.endpoints import router as offers_router
from app.user.endpoints import router as user_router


api_router = APIRouter()

api_router.include_router(
    user_router,
    prefix="/users",
    tags=["Usuários"],
)
api_router.include_router(
    establishment_router,
    prefix="/establishments",
    tags=["Estabelecimentos"],
)
api_router.include_router(
    disposals_router,
    prefix="/disposals",
    tags=["Descartes"],
)
api_router.include_router(
    trash_type_router,
    prefix="/trash_types",
    tags=["Tipos de lixo"],
)
api_router.include_router(
    offers_router,
    prefix="/offers",
    tags=["Ofertas"],
)
