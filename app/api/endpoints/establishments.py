from typing import List
from sqlalchemy.orm import Session
from fastapi import APIRouter, HTTPException, Depends


from app.database import get_db

from app.crud.ewaste import create_establishment, get_establishments, get_establishment
from app.schemas.ewaste import (
    Establishment,
    EstablishmentCreate,
    Establishment,
    Establishment,
)


router = APIRouter()


@router.post("/", response_model=Establishment)
def create_establishment_route(
    establishment: EstablishmentCreate, db: Session = Depends(get_db)
):
    return create_establishment(db=db, establishment=establishment)


@router.get("/", response_model=List[Establishment])
def read_establishments_route(
    skip: int = 0, limit: int = 100, db: Session = Depends(get_db)
):
    establishments = get_establishments(db, skip=skip, limit=limit)
    return establishments


@router.get("/{establishment_id}", response_model=Establishment)
def read_establishment_route(establishment_id: int, db: Session = Depends(get_db)):
    db_establishment = get_establishment(db, establishment_id=establishment_id)
    if db_establishment is None:
        raise HTTPException(status_code=404, detail="Establishment not found")
    return db_establishment
