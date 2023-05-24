from typing import List
from sqlalchemy.orm import Session
from fastapi import APIRouter, HTTPException, Depends

from app.database import get_db

from app.schemas.ewaste import TrashTypeCreate, TrashType
from app.crud.ewaste import create_trashtype, get_trashtypes, get_trashtype


router = APIRouter()


@router.post("/", response_model=TrashType)
def create_trashtype_route(trashtype: TrashTypeCreate, db: Session = Depends(get_db)):
    return create_trashtype(db=db, trashtype=trashtype)


@router.get("/", response_model=List[TrashType])
def read_trashtypes_route(
    skip: int = 0, limit: int = 100, db: Session = Depends(get_db)
):
    trashtypes = get_trashtypes(db, skip=skip, limit=limit)
    return trashtypes


@router.get("/{trashtype_id}", response_model=TrashType)
def read_trashtype_route(trashtype_id: int, db: Session = Depends(get_db)):
    db_trashtype = get_trashtype(db, trashtype_id=trashtype_id)
    if db_trashtype is None:
        raise HTTPException(status_code=404, detail="TrashType not found")
    return db_trashtype
