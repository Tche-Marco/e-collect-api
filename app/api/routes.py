from fastapi import APIRouter
from .endpoints import ewaste

router = APIRouter()

router.include_router(ewaste.router, prefix="/api")

# Other groups of routes, if necessary
