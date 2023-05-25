from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from app.database import Base

from app.models.user import User


class Establishment(Base):
    """
    Modelo da tabela Establishment no banco de dados. Representa um estabelecimento onde o lixo é descartado.

    Campos:
    - id: Um identificador único para o estabelecimento.
    - name: O nome do estabelecimento.
    - locale: A localização do estabelecimento.
    - disposals: Uma lista de descartes associados a este estabelecimento.
    """

    __tablename__ = "establishments"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    locale = Column(String)
    disposals = relationship("Disposal", back_populates="establishment")

    def __repr__(self):
        return f"{self.name} | {self.id}"


class TrashType(Base):
    """
    Modelo da tabela TrashType no banco de dados. Representa um tipo de lixo que pode ser descartado.

    Campos:
    - id: Um identificador único para o tipo de lixo.
    - name: O nome do tipo de lixo.
    """

    __tablename__ = "trashtypes"

    id = Column(Integer, primary_key=True)
    name = Column(String)

    def __repr__(self):
        return f"{self.name} | {self.id}"


class Disposal(Base):
    """
    Modelo da tabela Disposal no banco de dados. Representa um descarte de lixo feito por um usuário em um estabelecimento.

    Campos:
    - id: Um identificador único para o descarte.
    - quantity: A quantidade de lixo descartado.
    - user_id: O id do usuário que fez o descarte.
    - user: O usuário que fez o descarte.
    - establishment_id: O id do estabelecimento onde o lixo foi descartado.
    - establishment: O estabelecimento onde o lixo foi descartado.
    - trash_type_id: O id do tipo de lixo descartado.
    - trash_type: O tipo de lixo descartado.
    - punctuations: Uma lista de pontuações associadas a este descarte.
    """

    __tablename__ = "disposals"

    id = Column(Integer, primary_key=True)
    quantity = Column(Integer)
    user_id = Column(Integer, ForeignKey("users.id"))
    user = relationship("User", back_populates="disposals") #TODO: Conferir se é só importar User
    establishment_id = Column(Integer, ForeignKey("establishments.id"))
    establishment = relationship("Establishment", back_populates="disposals")
    trash_type_id = Column(Integer, ForeignKey("trashtypes.id"))
    trash_type = relationship("TrashType")
    punctuations = relationship("Punctuation", back_populates="disposal")

    def __repr__(self):
        return f"{self.establishment.name} | {self.trash_type.name} | {self.quantity}"


class Punctuation(Base):
    """
    Modelo da tabela Punctuation no banco de dados. Representa uma pontuação concedida para um descarte de lixo.

    Campos:
    - id: Um identificador único para a pontuação.
    - points: O número de pontos concedidos.
    - disposal_id: O id do descarte associado à pontuação.
    - disposal: O descarte associado à pontuação.
    """

    __tablename__ = "punctuations"

    id = Column(Integer, primary_key=True)
    points = Column(Integer)
    disposal_id = Column(Integer, ForeignKey("disposals.id"))
    disposal = relationship("Disposal", back_populates="punctuations")

    def __repr__(self):
        return f"Punctuation(id={self.id}, points={self.points})"
