from sqlalchemy.orm import Session
from typing import List, Optional

import app.offer.model as models
from app.offer.schema import (
    OfferCreate,
    OfferUpdate,
    Offer,
)


def get_offer(db: Session, offer_id: int) -> Optional[Offer]:
    """
    Função para obter uma oferta por id
    """
    db_offer = db.query(models.Offer).filter(models.Offer.id == offer_id).first()

    if db_offer is None:
        return None

    return Offer.from_orm(db_offer)


def get_offers(db: Session, skip: int = 0, limit: int = 100) -> List[Offer]:
    """
    Função para obter uma lista de ofertas
    """
    db_offers = db.query(models.Offer).offset(skip).limit(limit).all()

    return [Offer.from_orm(db_offer) for db_offer in db_offers]


def create_offer(db: Session, offer: OfferCreate) -> Offer:
    """
    Função para criar uma nova oferta
    """
    db_offer = models.Offer(**offer.dict())
    db.add(db_offer)
    db.commit()
    db.refresh(db_offer)

    return Offer.from_orm(db_offer)


def update_offer(db: Session, offer: OfferUpdate, offer_id: int) -> Optional[Offer]:
    """
    Função para atualizar uma oferta
    """
    db_offer = db.query(models.Offer).filter(models.Offer.id == offer_id).first()

    if db_offer is None:
        return None

    for var, value in vars(offer).items():
        setattr(db_offer, var, value) if value else None

    db.add(db_offer)
    db.commit()
    db.refresh(db_offer)

    return Offer.from_orm(db_offer)


def delete_offer(db: Session, offer_id: int) -> Optional[Offer]:
    """
    Função para deletar uma oferta
    """
    db_offer = db.query(models.Offer).filter(models.Offer.id == offer_id).first()

    if db_offer is None:
        return None

    db.delete(db_offer)
    db.commit()

    return Offer.from_orm(db_offer)
