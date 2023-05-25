from fastapi import APIRouter

from app.api.endpoints import (
    disposals,
)


api_router = APIRouter()

api_router.include_router(
    disposals.router,
    prefix="/disposals",
    tags=["disposals"],
)
