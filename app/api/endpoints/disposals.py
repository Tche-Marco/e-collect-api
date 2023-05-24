from typing import List
from sqlalchemy.orm import Session
from fastapi import APIRouter, HTTPException, Depends

from app.database import get_db

from app.crud.ewaste import create_disposal, get_disposals, get_disposal
from app.schemas.ewaste import (
    Disposal,
    DisposalCreate,
    Disposal,
    Disposal,
)


router = APIRouter()


@router.post("/", response_model=Disposal)
def create_disposal_route(disposal: DisposalCreate, db: Session = Depends(get_db)):
    return create_disposal(db=db, disposal=disposal)


@router.get("/", response_model=List[Disposal])
def read_disposals_route(
    skip: int = 0, limit: int = 100, db: Session = Depends(get_db)
):
    disposals = get_disposals(db, skip=skip, limit=limit)
    return disposals


@router.get("/{disposal_id}", response_model=Disposal)
def read_disposal_route(disposal_id: int, db: Session = Depends(get_db)):
    db_disposal = get_disposal(db, disposal_id=disposal_id)
    if db_disposal is None:
        raise HTTPException(status_code=404, detail="Disposal not found")
    return db_disposal
