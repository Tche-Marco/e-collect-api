from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.crud.ewaste import create_disposal
from app.models.ewaste import Disposal
from app.schemas.ewaste import DisposalCreate
from app.database import get_db

router = APIRouter()


@router.get("/disposal")
def get_disposals(db: Session = Depends(get_db)):
    """
    Endpoint para listar todos os descartes de lixo.
    """
    try:
        disposals = db.query(Disposal).all()
    except:
        disposals = {"message": "Nenhum descarte encontrado"}

    return disposals


@router.post("/disposal")
def dispose_waste(disposal: DisposalCreate, db: Session = Depends(get_db)):
    """
    Endpoint para realizar o descarte de lixo em um estabelecimento.
    """
    create_disposal(db, disposal)
    return {"message": "Descarte realizado com sucesso"}
