from sqlalchemy.orm import Session
from typing import List, Optional

import app.core.establishment.model as models
from app.core.establishment.schema import (
    EstablishmentCreate,
    EstablishmentUpdate,
    Establishment,
)


def get_establishment(db: Session, establishment_id: int) -> Optional[Establishment]:
    """
    Função para obter um estabelecimento por id
    """
    db_establishment = (
        db.query(models.Establishment)
        .filter(models.Establishment.id == establishment_id)
        .first()
    )

    if db_establishment is None:
        return None

    return Establishment.from_orm(db_establishment)


def get_establishments(
    db: Session, skip: int = 0, limit: int = 100
) -> List[Establishment]:
    """
    Função para obter uma lista de estabelecimentos
    O parâmetro 'skip' pula um número de linhas, 'limit' limita o número total de linhas retornadas.
    """
    db_establishments = db.query(models.Establishment).offset(skip).limit(limit).all()

    return [
        Establishment.from_orm(db_establishment)
        for db_establishment in db_establishments
    ]


def create_establishment(
    db: Session, establishment: EstablishmentCreate
) -> Establishment:
    """
    Função para criar um novo estabelecimento
    """
    db_establishment = models.Establishment(**establishment.dict())
    db.add(db_establishment)
    db.commit()
    db.refresh(db_establishment)

    return Establishment.from_orm(db_establishment)


def update_establishment(
    db: Session, establishment: EstablishmentUpdate, establishment_id: int
) -> Optional[Establishment]:
    """
    Função para atualizar um estabelecimento
    """
    db_establishment = (
        db.query(models.Establishment)
        .filter(models.Establishment.id == establishment_id)
        .first()
    )

    if db_establishment is None:
        return None

    for var, value in vars(establishment).items():
        setattr(db_establishment, var, value) if value else None

    db.add(db_establishment)
    db.commit()
    db.refresh(db_establishment)

    return Establishment.from_orm(db_establishment)


def delete_establishment(db: Session, establishment_id: int) -> Optional[Establishment]:
    """
    Função para deletar um estabelecimento
    """
    db_establishment = (
        db.query(models.Establishment)
        .filter(models.Establishment.id == establishment_id)
        .first()
    )

    if db_establishment is None:
        return None

    db.delete(db_establishment)
    db.commit()

    return Establishment.from_orm(db_establishment)
