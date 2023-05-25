from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from app.database import Base


class User(Base):
    """
    Modelo para representar um usuário no banco de dados.

    Campos:
    - id: Um identificador único para o usuário.
    - name: O nome do usuário.
    - disposals: lista dos descartes feitos por este usuário.
    """

    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)

    disposals = relationship("Disposal", back_populates="user")

    def __repr__(self):
        return f"{self.name} | {self.id})"
