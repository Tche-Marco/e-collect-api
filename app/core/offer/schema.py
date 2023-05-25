from typing import Optional
from pydantic import BaseModel


class OfferBase(BaseModel):
    """
    Classe base para a oferta, incluindo atributos comuns para criação e leitura.
    """

    target: float
    product_description: str
    is_active: bool


class OfferCreate(OfferBase):
    """
    Schema para criação de oferta. Herda de OfferBase e inclui o id do estabelecimento.
    """

    establishment_id: int


class OfferUpdate(OfferBase):
    """
    Schema para atualização de oferta. Herda de OfferBase e permite atualizar todos os campos.
    """

    target: Optional[float] = None
    product_description: Optional[str] = None
    is_active: Optional[bool] = None
    establishment_id: Optional[int] = None


class Offer(OfferBase):
    """
    Schema para leitura de oferta. Herda de OfferBase e inclui o id da oferta e do estabelecimento.
    """

    id: int
    establishment_id: int

    class Config:
        orm_mode = True
