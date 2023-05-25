from typing import List
from sqlalchemy.orm import Session
from fastapi import APIRouter, HTTPException, Depends

from app.core.database import get_db
from app.core.establishment.schema import (
    Establishment,
    EstablishmentCreate,
    EstablishmentUpdate,
)
from app.core.establishment.functions import (
    get_establishment,
    get_establishments,
    create_establishment,
    update_establishment,
    delete_establishment,
)


router = APIRouter()


@router.post("/", response_model=Establishment)
def create_establishment_route(
    establishment: EstablishmentCreate, db: Session = Depends(get_db)
):
    db_establishment = get_establishment(db, establishment_id=establishment.id)

    if db_establishment:
        raise HTTPException(status_code=400, detail="Estabelecimento já existe!")

    return create_establishment(db=db, establishment=establishment)


@router.get("/", response_model=List[Establishment])
def get_establishments_route(
    skip: int = 0, limit: int = 100, db: Session = Depends(get_db)
):
    establishments = get_establishments(db, skip=skip, limit=limit)

    return establishments


@router.get("/{establishment_id}", response_model=Establishment)
def get_establishment_route(establishment_id: int, db: Session = Depends(get_db)):
    db_establishment = get_establishment(db, establishment_id=establishment_id)

    if db_establishment is None:
        raise HTTPException(status_code=404, detail="Estabelecimento não encontrado!")

    return db_establishment


@router.put("/{establishment_id}", response_model=Establishment)
def update_establishment_route(
    establishment_id: int,
    establishment: EstablishmentUpdate,
    db: Session = Depends(get_db),
):
    db_establishment = update_establishment(
        db, establishment_id=establishment_id, establishment=establishment
    )

    if db_establishment is None:
        raise HTTPException(status_code=404, detail="Estabelecimento não encontrado!")

    return db_establishment


@router.delete("/{establishment_id}", response_model=Establishment)
def delete_establishment_route(establishment_id: int, db: Session = Depends(get_db)):
    db_establishment = delete_establishment(db, establishment_id=establishment_id)

    if db_establishment is None:
        raise HTTPException(status_code=404, detail="Estabelecimento não encontrado!")

    return db_establishment
