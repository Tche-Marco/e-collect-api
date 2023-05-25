from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from app.core.database import Base


class TrashType(Base):
    """
    Modelo para representar um tipo de lixo no banco de dados.

    Campos:
    - id: Um identificador único para o tipo de lixo.
    - name: O nome do tipo de lixo.
    - value: O valor unitário do tipo de lixo.
    - disposals: lista dos descartes associados a este tipo de lixo.
    """

    __tablename__ = "trash_types"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    value = Column(Integer, index=True)

    disposals = relationship("Disposal", back_populates="trash_type")

    def __repr__(self):
        return f"{self.name} | {self.id} | {self.value}"
