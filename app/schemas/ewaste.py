from pydantic import BaseModel


class DisposalCreate(BaseModel):
    """
    Esquema de validação para a criação de um novo registro de descarte.
    """

    user_id: int
    establishment_id: int
    waste_id: int
    quantity: int


# Other validation schemas, if necessary
