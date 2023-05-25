from sqlalchemy.orm import Session
from typing import List, Optional

import app.trash_type.model as models
from app.trash_type.schema import (
    TrashTypeCreate,
    TrashTypeUpdate,
    TrashType,
)


def get_trash_type(db: Session, trash_type_id: int) -> Optional[TrashType]:
    """
    Função para obter um tipo de lixo por id
    """
    db_trash_type = (
        db.query(models.TrashType).filter(models.TrashType.id == trash_type_id).first()
    )

    if db_trash_type is None:
        return None

    return TrashType.from_orm(db_trash_type)


def get_trash_types(db: Session, skip: int = 0, limit: int = 100) -> List[TrashType]:
    """
    Função para obter uma lista de tipos de lixo
    O parâmetro 'skip' pula um número de linhas, 'limit' limita o número total de linhas retornadas.
    """
    db_trash_types = db.query(models.TrashType).offset(skip).limit(limit).all()

    return [TrashType.from_orm(db_trash_type) for db_trash_type in db_trash_types]


def create_trash_type(db: Session, trash_type: TrashTypeCreate) -> TrashType:
    """
    Função para criar um novo tipo de lixo
    """
    db_trash_type = models.TrashType(name=trash_type.name, value=trash_type.value)
    db.add(db_trash_type)
    db.commit()
    db.refresh(db_trash_type)

    return TrashType.from_orm(db_trash_type)


def update_trash_type(
    db: Session, trash_type: TrashTypeUpdate, trash_type_id: int
) -> Optional[TrashType]:
    """
    Função para atualizar um tipo de lixo
    """
    db_trash_type = (
        db.query(models.TrashType).filter(models.TrashType.id == trash_type_id).first()
    )

    if db_trash_type is None:
        return None

    for var, value in vars(trash_type).items():
        setattr(db_trash_type, var, value) if value else None

    db.add(db_trash_type)
    db.commit()
    db.refresh(db_trash_type)

    return TrashType.from_orm(db_trash_type)


def delete_trash_type(db: Session, trash_type_id: int) -> Optional[TrashType]:
    """
    Função para deletar um tipo de lixo
    """
    db_trash_type = (
        db.query(models.TrashType).filter(models.TrashType.id == trash_type_id).first()
    )

    if db_trash_type is None:
        return None

    db.delete(db_trash_type)
    db.commit()

    return TrashType.from_orm(db_trash_type)
