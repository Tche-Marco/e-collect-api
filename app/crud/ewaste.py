from sqlalchemy.orm import Session

from app.models.ewaste import TrashType, Disposal, Punctuation


from app.schemas.ewaste import (
    TrashTypeCreate,
    DisposalCreate,
    PunctuationCreate,
)


def get_trashtype(db: Session, trashtype_id: int):
    """
    Obtém um tipo de lixo pelo seu id.
    """
    return db.query(TrashType).filter(TrashType.id == trashtype_id).first()


def get_trashtypes(db: Session, skip: int = 0, limit: int = 100):
    """
    Obtém uma lista de tipos de lixo.
    O parâmetro 'skip' pula um número de linhas, 'limit' limita o número total de linhas retornadas.
    """
    return db.query(TrashType).offset(skip).limit(limit).all()


def create_trashtype(db: Session, trashtype: TrashTypeCreate):
    """
    Cria um novo tipo de lixo.
    """
    db_trashtype = TrashType(**trashtype.dict())
    db.add(db_trashtype)
    db.commit()
    db.refresh(db_trashtype)

    return db_trashtype


def get_disposal(db: Session, disposal_id: int):
    """
    Obtém um descarte pelo seu id.
    """
    return db.query(Disposal).filter(Disposal.id == disposal_id).first()


def get_disposals(db: Session, skip: int = 0, limit: int = 100):
    """
    Obtém uma lista de descartes.
    O parâmetro 'skip' pula um número de linhas, 'limit' limita o número total de linhas retornadas.
    """
    return db.query(Disposal).offset(skip).limit(limit).all()


def create_disposal(db: Session, disposal: DisposalCreate):
    """
    Cria um novo descarte.
    """
    db_disposal = Disposal(**disposal.dict())
    db.add(db_disposal)
    db.commit()
    db.refresh(db_disposal)

    return db_disposal


def get_punctuation(db: Session, punctuation_id: int):
    """
    Obtém uma pontuação pelo seu id.
    """
    return db.query(Punctuation).filter(Punctuation.id == punctuation_id).first()


def get_punctuations(db: Session, skip: int = 0, limit: int = 100):
    """
    Obtém uma lista de pontuações.
    O parâmetro 'skip' pula um número de linhas, 'limit' limita o número total de linhas retornadas.
    """
    return db.query(Punctuation).offset(skip).limit(limit).all()


def create_punctuation(db: Session, punctuation: PunctuationCreate):
    """
    Cria uma nova pontuação.
    """
    db_punctuation = Punctuation(**punctuation.dict())
    db.add(db_punctuation)
    db.commit()
    db.refresh(db_punctuation)

    return db_punctuation
