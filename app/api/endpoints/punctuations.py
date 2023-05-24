from typing import List
from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session


from app.database import get_db
from app.crud.ewaste import create_punctuation, get_punctuations, get_punctuation
from app.schemas.ewaste import Punctuation, PunctuationCreate, Punctuation, Punctuation


router = APIRouter()


@router.post("/", response_model=Punctuation)
def create_punctuation_route(
    punctuation: PunctuationCreate, db: Session = Depends(get_db)
):
    return create_punctuation(db=db, punctuation=punctuation)


@router.get("/", response_model=List[Punctuation])
def read_punctuations_route(
    skip: int = 0, limit: int = 100, db: Session = Depends(get_db)
):
    punctuations = get_punctuations(db, skip=skip, limit=limit)
    return punctuations


@router.get("/{punctuation_id}", response_model=Punctuation)
def read_punctuation_route(punctuation_id: int, db: Session = Depends(get_db)):
    db_punctuation = get_punctuation(db, punctuation_id=punctuation_id)
    if db_punctuation is None:
        raise HTTPException(status_code=404, detail="Punctuation not found")
    return db_punctuation
