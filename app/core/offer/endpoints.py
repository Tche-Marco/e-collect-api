from typing import List
from sqlalchemy.orm import Session
from fastapi import APIRouter, HTTPException, Depends

from app.core.offer.schema import Offer, OfferCreate, OfferUpdate
from app.core.database import get_db
from app.core.offer.functions import (
    get_offer,
    get_offers,
    create_offer,
    update_offer,
    delete_offer,
)


router = APIRouter()


@router.post("/", response_model=Offer)
def create_offer_route(offer: OfferCreate, db: Session = Depends(get_db)):
    return create_offer(db=db, offer=offer)


@router.get("/", response_model=List[Offer])
def get_offers_route(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    offers = get_offers(db, skip=skip, limit=limit)

    return offers


@router.get("/{offer_id}", response_model=Offer)
def get_offer_route(offer_id: int, db: Session = Depends(get_db)):
    db_offer = get_offer(db, offer_id=offer_id)

    if db_offer is None:
        raise HTTPException(status_code=404, detail="Oferta não encontrada!")

    return db_offer


@router.put("/{offer_id}", response_model=Offer)
def update_offer_route(
    offer_id: int, offer: OfferUpdate, db: Session = Depends(get_db)
):
    db_offer = update_offer(db, offer_id=offer_id, offer=offer)

    if db_offer is None:
        raise HTTPException(status_code=404, detail="Oferta não encontrada!")

    return db_offer


@router.delete("/{offer_id}", response_model=Offer)
def delete_offer_route(offer_id: int, db: Session = Depends(get_db)):
    db_offer = delete_offer(db, offer_id=offer_id)

    if db_offer is None:
        raise HTTPException(status_code=404, detail="Oferta não encontrada!")

    return db_offer
