from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from app.database import Base


class Establishment(Base):
    """
    Modelo para representar um estabelecimento no banco de dados.

    Campos:
    - id: Um identificador único para o estabelecimento.
    - name: O nome do estabelecimento.
    - location: A localização do estabelecimento.
    - photo_url: URL da foto do estabelecimento.
    - phone: Telefone do estabelecimento.
    - summary: Informações resumidas sobre o estabelecimento.
    - more_info: Informações detalhadas sobre o estabelecimento.
    - disposals: lista dos descartes feitos no estabelecimento.
    - offers: ofertas do estabelecimento.
    """

    __tablename__ = "establishments"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    location = Column(String, index=True)
    photo_url = Column(String, nullable=True)
    phone = Column(String)
    summary = Column(String)
    more_info = Column(String)

    disposals = relationship("Disposal", back_populates="establishment")
    offers = relationship("Offer", back_populates="establishment")

    def __repr__(self):
        return f"{self.name} | {self.id}"
