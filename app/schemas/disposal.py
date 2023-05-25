from typing import Optional
from pydantic import BaseModel


class DisposalBase(BaseModel):
    """
    Classe base para o descarte, incluindo atributos comuns para criação e leitura.
    """

    amount: float


class DisposalCreate(DisposalBase):
    """
    Schema para criação de descarte. Herda de DisposalBase e inclui o id do tipo de lixo e do usuário.
    """

    establishment_id: int
    trash_type_id: int
    user_id: int


class DisposalUpdate(DisposalBase):
    """
    Schema para atualização de descarte. Herda de DisposalBase e permite atualizar todos os campos.
    """

    amount: Optional[float] = None
    establishment_id: Optional[int] = None
    trash_type_id: Optional[int] = None
    user_id: Optional[int] = None


class Disposal(DisposalBase):
    """
    Schema para leitura de descarte. Herda de DisposalBase e inclui o id do descarte, do tipo de lixo e do usuário.
    """

    id: int
    establishment_id: int
    trash_type_id: int
    user_id: int

    class Config:
        orm_mode = True
