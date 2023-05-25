from typing import Optional, List
from pydantic import BaseModel

from app.disposal.schema import Disposal
from app.offer.schema import Offer


class EstablishmentBase(BaseModel):
    """
    Classe base para o estabelecimento, incluindo atributos comuns para criação e leitura.
    """

    name: str
    location: str
    phone: str
    summary: str
    more_info: str
    photo_url: Optional[str] = None


class EstablishmentCreate(EstablishmentBase):
    """
    Schema para criação de estabelecimento. Herda de EstablishmentBase e inclui id.
    """

    id: Optional[int]


class EstablishmentUpdate(EstablishmentBase):
    """
    Schema para atualização de estabelecimento. Herda de EstablishmentBase.
    Se um campo não for fornecido, o estabelecimento será atualizado com o valor atual.
    """

    name: Optional[str] = None
    location: Optional[str] = None
    phone: Optional[str] = None
    summary: Optional[str] = None
    more_info: Optional[str] = None
    photo_url: Optional[str] = None


class Establishment(EstablishmentBase):
    """
    Schema para leitura de estabelecimento. Herda de EstablishmentBase e inclui o id do estabelecimento.
    """

    id: int
    disposals: List[Disposal] = []
    offers: List[Offer] = []

    class Config:
        orm_mode = True
