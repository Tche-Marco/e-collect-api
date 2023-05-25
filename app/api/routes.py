from fastapi import APIRouter

from app.api.endpoints import (
    users,
    establishments,
    trash_types,
    disposals,
    offers,
)


api_router = APIRouter()

api_router.include_router(
    users.router,
    prefix="/users",
    tags=["users"],
)
api_router.include_router(
    establishments.router,
    prefix="/establishments",
    tags=["establishments"],
)
api_router.include_router(
    trash_types.router,
    prefix="/trash_types",
    tags=["trash_types"],
)
api_router.include_router(
    disposals.router,
    prefix="/disposals",
    tags=["disposals"],
)
api_router.include_router(
    offers.router,
    prefix="/offers",
    tags=["offers"],
)
