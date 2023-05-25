from sqlalchemy.orm import Session
from typing import List, Optional

import app.models.disposal as models
from app.schemas.disposal import (
    DisposalCreate,
    DisposalUpdate,
    Disposal,
)


def get_disposal(db: Session, disposal_id: int) -> Optional[Disposal]:
    """
    Função para obter um descarte por id
    """
    db_disposal = (
        db.query(models.Disposal).filter(models.Disposal.id == disposal_id).first()
    )

    if db_disposal is None:
        return None

    return Disposal.from_orm(db_disposal)


def get_disposals(db: Session, skip: int = 0, limit: int = 100) -> List[Disposal]:
    """
    Função para obter uma lista de descartes
    """
    db_disposals = db.query(models.Disposal).offset(skip).limit(limit).all()

    return [Disposal.from_orm(db_disposal) for db_disposal in db_disposals]


def create_disposal(db: Session, disposal: DisposalCreate) -> Disposal:
    """
    Função para criar um novo descarte
    """
    db_disposal = models.Disposal(**disposal.dict())
    db.add(db_disposal)
    db.commit()
    db.refresh(db_disposal)

    return Disposal.from_orm(db_disposal)


def update_disposal(
    db: Session, disposal: DisposalUpdate, disposal_id: int
) -> Optional[Disposal]:
    """
    Função para atualizar um descarte
    """
    db_disposal = (
        db.query(models.Disposal).filter(models.Disposal.id == disposal_id).first()
    )

    if db_disposal is None:
        return None

    for var, value in vars(disposal).items():
        setattr(db_disposal, var, value) if value else None

    db.add(db_disposal)
    db.commit()
    db.refresh(db_disposal)

    return Disposal.from_orm(db_disposal)


def delete_disposal(db: Session, disposal_id: int) -> Optional[Disposal]:
    """
    Função para deletar um descarte
    """
    db_disposal = (
        db.query(models.Disposal).filter(models.Disposal.id == disposal_id).first()
    )

    if db_disposal is None:
        return None

    db.delete(db_disposal)
    db.commit()

    return Disposal.from_orm(db_disposal)
