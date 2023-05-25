from typing import Optional, List
from pydantic import BaseModel

from app.core.disposal.schema import Disposal


class UserBase(BaseModel):
    """
    Classe base para o usuário, incluindo atributos comuns para criação e leitura.
    """

    name: str


class UserCreate(UserBase):
    """
    Schema para criação de usuário. Herda de UserBase e inclui senha.
    """

    id: Optional[int]


class UserUpdate(UserBase):
    """
    Schema para atualização de usuário. Herda de UserBase e inclui senha opcional.
    Se a senha não for fornecida, o usuário será atualizado com a senha atual.
    """

    name: Optional[str] = None


class User(UserBase):
    """
    Schema para leitura de usuário. Herda de UserBase e inclui o id do usuário.
    """

    id: int
    disposals: List[Disposal] = []

    class Config:
        orm_mode = True
