from sqlalchemy.orm import Session
from werkzeug.security import generate_password_hash

from app.models.ewaste import User, Establishment, TrashType, Disposal, Punctuation
from app.schemas.ewaste import (
    UserCreate,
    UserUpdate,
    EstablishmentCreate,
    TrashTypeCreate,
    DisposalCreate,
    PunctuationCreate,
)


def get_user(db: Session, user_id: int):
    """
    Obtém um usuário pelo seu id.
    """
    return db.query(User).filter(User.id == user_id).first()


def get_user_by_email(db: Session, email: str):
    """
    Obtém um usuário pelo seu email.
    """
    return db.query(User).filter(User.email == email).first()


def get_users(db: Session, skip: int = 0, limit: int = 100):
    """
    Obtém uma lista de usuários.
    O parâmetro 'skip' pula um número de linhas, 'limit' limita o número total de linhas retornadas.
    """
    return db.query(User).offset(skip).limit(limit).all()


def create_user(db: Session, user: UserCreate):
    """
    Cria um novo usuário.
    """
    hashed_password = generate_password_hash(user.password)
    db_user = User(**user.dict(), password_hash=hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def update_user(db: Session, user: UserUpdate, user_id: int):
    """
    Atualiza um usuário existente.
    """
    db_user = get_user(db, user_id)

    if db_user is None:
        return None

    user_data = user.dict()

    for key, value in user_data.items():
        setattr(db_user, key, value)

    db.commit()
    db.refresh(db_user)

    return db_user


def delete_user(db: Session, user_id: int):
    """
    Deleta um usuário existente.
    """
    db_user = get_user(db, user_id)

    if db_user is None:
        return None

    db.delete(db_user)
    db.commit()

    return db_user


def get_establishment(db: Session, establishment_id: int):
    """
    Obtém um estabelecimento pelo seu id.
    """
    return db.query(Establishment).filter(Establishment.id == establishment_id).first()


def get_establishments(db: Session, skip: int = 0, limit: int = 100):
    """
    Obtém uma lista de estabelecimentos.
    O parâmetro 'skip' pula um número de linhas, 'limit' limita o número total de linhas retornadas.
    """
    return db.query(Establishment).offset(skip).limit(limit).all()


def create_establishment(db: Session, establishment: EstablishmentCreate):
    """
    Cria um novo estabelecimento.
    """
    db_establishment = Establishment(**establishment.dict())
    db.add(db_establishment)
    db.commit()
    db.refresh(db_establishment)

    return db_establishment


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
