from typing import List
from sqlalchemy.orm import Session
from fastapi import APIRouter, HTTPException, Depends

from app.database import get_db

from app.schemas.trash_type import TrashType, TrashTypeCreate, TrashTypeUpdate
from app.crud.trash_type import (
    get_trash_type,
    get_trash_types,
    create_trash_type,
    update_trash_type,
    delete_trash_type,
)


router = APIRouter()


@router.post("/", response_model=TrashType)
def create_trash_type_route(trash_type: TrashTypeCreate, db: Session = Depends(get_db)):
    db_trash_type = get_trash_type(db, trash_type_id=trash_type.id)

    if db_trash_type:
        raise HTTPException(status_code=400, detail="Tipo de lixo já existe!")

    return create_trash_type(db=db, trash_type=trash_type)


@router.get("/", response_model=List[TrashType])
def get_trash_types_route(
    skip: int = 0, limit: int = 100, db: Session = Depends(get_db)
):
    trash_types = get_trash_types(db, skip=skip, limit=limit)

    return trash_types


@router.get("/{trash_type_id}", response_model=TrashType)
def get_trash_type_route(trash_type_id: int, db: Session = Depends(get_db)):
    db_trash_type = get_trash_type(db, trash_type_id=trash_type_id)

    if db_trash_type is None:
        raise HTTPException(status_code=404, detail="Tipo de lixo não encontrado!")

    return db_trash_type


@router.put("/{trash_type_id}", response_model=TrashType)
def update_trash_type_route(
    trash_type_id: int, trash_type: TrashTypeUpdate, db: Session = Depends(get_db)
):
    db_trash_type = update_trash_type(
        db, trash_type_id=trash_type_id, trash_type=trash_type
    )

    if db_trash_type is None:
        raise HTTPException(status_code=404, detail="Tipo de lixo não encontrado!")

    return db_trash_type


@router.delete("/{trash_type_id}", response_model=TrashType)
def delete_trash_type_route(trash_type_id: int, db: Session = Depends(get_db)):
    db_trash_type = delete_trash_type(db, trash_type_id=trash_type_id)

    if db_trash_type is None:
        raise HTTPException(status_code=404, detail="Tipo de lixo não encontrado!")

    return db_trash_type
