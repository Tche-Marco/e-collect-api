from fastapi import APIRouter

from app.api.endpoints import users, establishments, trashtypes, disposals, punctuations


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
    trashtypes.router,
    prefix="/trashtypes",
    tags=["trashtypes"],
)
api_router.include_router(
    disposals.router,
    prefix="/disposals",
    tags=["disposals"],
)
api_router.include_router(
    punctuations.router,
    prefix="/punctuations",
    tags=["punctuations"],
)
