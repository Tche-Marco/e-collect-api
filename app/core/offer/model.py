from sqlalchemy import Column, Integer, String, Boolean, Float, ForeignKey
from sqlalchemy.orm import relationship
from app.core.database import Base


class Offer(Base):
    """
    Modelo para representar uma oferta no banco de dados.

    Campos:
    - id: Um identificador único para a oferta.
    - target: Objetivo de pontos para liberar a oferta.
    - product_description: descrição do produto que a oferta está 'vendendo'.
    - is_active: Indica se oferta está ativa.
    - establishment_id: Id do estabelecimento que a oferta pertence.
    """

    __tablename__ = "offers"

    id = Column(Integer, primary_key=True, index=True)
    target = Column(Float, index=True)
    product_description = Column(String)
    is_active = Column(Boolean)
    establishment_id = Column(Integer, ForeignKey("establishments.id"))

    establishment = relationship("Establishment", back_populates="offers")

    def __repr__(self):
        return f"{self.product_description} | {self.target} | {self.is_active}"
