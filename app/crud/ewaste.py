from sqlalchemy.orm import Session
from app.models.ewaste import Disposal
from app.schemas.ewaste import DisposalCreate


def create_disposal(db: Session, disposal: DisposalCreate):
    """
    Função para criar um novo registro de descarte no banco de dados.
    """
    db_disposal = Disposal(
        user_id=disposal.user_id,
        establishment_id=disposal.establishment_id,
        waste_id=disposal.waste_id,
        quantity=disposal.quantity,
    )
    db.add(db_disposal)
    db.commit()
    db.refresh(db_disposal)
    return db_disposal


# Other CRUD functions and their respective logic
