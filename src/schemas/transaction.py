import enum
from pydantic import BaseModel, PositiveFloat

class TransactionType(str, enum.Enum):
    DEPOSIT = "deposito"
    WITHDRAWAL = "saque"

# Esquema para validar depósitos e saques da API Bancária
class TransactionIn(BaseModel):
    account_id: int
    type: TransactionType
    amount: PositiveFloat # Bloqueia valores negativos ou zerados
