from sqlalchemy import Column, Integer, Float, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base


class Disposal(Base):
    """
    Modelo para representar um descarte no banco de dados.

    Campos:
    - id: Um identificador único para o descarte.
    - amount: quantidade de lixo descartada.
    - trash_type_id: Id do tipo de lixo descartado.
    - user_id: Id do usuário que realizou o descarte.
    """

    __tablename__ = "disposals"

    id = Column(Integer, primary_key=True, index=True)
    amount = Column(Float, index=True)
    trash_type_id = Column(Integer, ForeignKey("trash_types.id"))
    user_id = Column(Integer, ForeignKey("users.id"))

    trash_type = relationship("TrashType", back_populates="disposals")
    user = relationship("User", back_populates="disposals")

    def __repr__(self):
        return f"{self.trash_type.name} | {self.amount}"
