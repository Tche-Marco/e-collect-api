from typing import List
from sqlalchemy.orm import Session
from fastapi import APIRouter, HTTPException, Depends

from app.core.database import get_db
from app.disposal.schema import Disposal, DisposalCreate, DisposalUpdate
from app.disposal.functions import (
    get_disposal,
    get_disposals,
    create_disposal,
    update_disposal,
    delete_disposal,
)


router = APIRouter()


@router.post("/", response_model=Disposal)
def create_disposal_route(disposal: DisposalCreate, db: Session = Depends(get_db)):
    return create_disposal(db=db, disposal=disposal)


@router.get("/", response_model=List[Disposal])
def get_disposals_route(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    disposals = get_disposals(db, skip=skip, limit=limit)

    return disposals


@router.get("/{disposal_id}", response_model=Disposal)
def get_disposal_route(disposal_id: int, db: Session = Depends(get_db)):
    db_disposal = get_disposal(db, disposal_id=disposal_id)

    if db_disposal is None:
        raise HTTPException(status_code=404, detail="Descarte não encontrado!")

    return db_disposal


@router.put("/{disposal_id}", response_model=Disposal)
def update_disposal_route(
    disposal_id: int, disposal: DisposalUpdate, db: Session = Depends(get_db)
):
    db_disposal = update_disposal(db, disposal_id=disposal_id, disposal=disposal)

    if db_disposal is None:
        raise HTTPException(status_code=404, detail="Descarte não encontrado!")

    return db_disposal


@router.delete("/{disposal_id}", response_model=Disposal)
def delete_disposal_route(disposal_id: int, db: Session = Depends(get_db)):
    db_disposal = delete_disposal(db, disposal_id=disposal_id)

    if db_disposal is None:
        raise HTTPException(status_code=404, detail="Descarte não encontrado!")

    return db_disposal
