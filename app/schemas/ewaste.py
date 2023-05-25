from typing import Optional, List
from pydantic import BaseModel

from app.schemas.user import User
from app.schemas.establishment import Establishment


# ----- TrashType Schemas -----


class TrashTypeBase(BaseModel):
    """
    Classe base para tipo de lixo, incluindo atributos comuns para criação e leitura.
    """

    name: str


class TrashTypeCreate(TrashTypeBase):
    """
    Schema para criação de tipo de lixo. Herda de TrashTypeBase.
    """

    pass


class TrashType(TrashTypeBase):
    """
    Schema para leitura de tipo de lixo. Herda de TrashTypeBase e inclui o id do tipo de lixo.
    """

    id: int

    class Config:
        orm_mode = True


# ----- Disposal Schemas -----


class DisposalBase(BaseModel):
    """
    Classe base para descarte, incluindo atributos comuns para criação e leitura.
    """

    quantity: int


class DisposalCreate(DisposalBase):
    """
    Schema para criação de descarte. Herda de DisposalBase e inclui o id do usuário, do estabelecimento e do tipo de lixo.
    """

    user_id: int
    establishment_id: int
    trash_type_id: int


class Disposal(DisposalBase):
    """
    Schema para leitura de descarte. Herda de DisposalBase e inclui o id do descarte e as informações do usuário, do estabelecimento e do tipo de lixo.
    """

    id: int
    user: User
    establishment: Establishment
    trash_type: TrashType

    class Config:
        orm_mode = True


# ----- Punctuation Schemas -----


class PunctuationBase(BaseModel):
    """
    Classe base para pontuação, incluindo atributos comuns para criação e leitura.
    """

    points: int


class PunctuationCreate(PunctuationBase):
    """
    Schema para criação de pontuação. Herda de PunctuationBase e inclui o id do descarte.
    """

    disposal_id: int


class Punctuation(PunctuationBase):
    """
    Schema para leitura de pontuação. Herda de PunctuationBase e inclui o id da pontuação e as informações do descarte.
    """

    id: int
    disposal: Disposal

    class Config:
        orm_mode = True
