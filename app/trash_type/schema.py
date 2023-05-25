from typing import Optional, List
from pydantic import BaseModel

from app.disposal.schema import Disposal


class TrashTypeBase(BaseModel):
    """
    Classe base para o tipo de lixo, incluindo atributos comuns para criação e leitura.
    """

    name: str
    value: int


class TrashTypeCreate(TrashTypeBase):
    """
    Schema para criação de tipo de lixo. Herda de TrashTypeBase.
    """

    id: Optional[int]


class TrashTypeUpdate(TrashTypeBase):
    """
    Schema para atualização de tipo de lixo. Herda de TrashTypeBase e inclui atributos opcionais.
    Se um atributo não for fornecido, o tipo de lixo será atualizado com o valor atual.
    """

    name: Optional[str] = None
    value: Optional[int] = None


class TrashType(TrashTypeBase):
    """
    Schema para leitura de tipo de lixo. Herda de TrashTypeBase e inclui o id do tipo de lixo.
    """

    id: int
    disposals: List[Disposal] = []

    class Config:
        orm_mode = True
