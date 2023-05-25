from fastapi import APIRouter

from app.api.endpoints import (
    disposals,
    offers,
)


api_router = APIRouter()


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
