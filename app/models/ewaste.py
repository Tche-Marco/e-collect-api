from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from app.database import Base


class UserEstablishmentScore(Base):
    """
    Classe que representa a pontuação do usuário em um estabelecimento.
    """

    __tablename__ = "user_establishment_score"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("user.id"))
    establishment_id = Column(Integer, ForeignKey("establishment.id"))
    score = Column(Integer)


class User(Base):
    """
    Classe que representa um usuário.
    """

    __tablename__ = "user"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)

    disposals = relationship("Disposal", back_populates="user")


class Establishment(Base):
    """
    Classe que representa um estabelecimento.
    """

    __tablename__ = "establishment"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)

    disposals = relationship("Disposal", back_populates="establishment")
    scores = relationship("UserEstablishmentScore", back_populates="establishment")


class Disposal(Base):
    """
    Classe que representa um descarte de lixo.
    """

    __tablename__ = "disposal"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("user.id"))
    establishment_id = Column(Integer, ForeignKey("establishment.id"))
    waste_id = Column(Integer, ForeignKey("waste.id"))
    quantity = Column(Integer)

    user = relationship("User", back_populates="disposals")
    establishment = relationship("Establishment", back_populates="disposals")
    waste = relationship("Waste", back_populates="disposals")


class Waste(Base):
    """
    Classe que representa um tipo de lixo.
    """

    __tablename__ = "waste"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)

    disposals = relationship("Disposal", back_populates="waste")
