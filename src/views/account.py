from pydantic import BaseModel, AwareDatetime, NaiveDatetime
from decimal import Decimal

# Estrutura de resposta pública para dados da conta corrente
class AccountOut(BaseModel):
    id: int
    user_id: int
    balance: Decimal
    created_at: AwareDatetime | NaiveDatetime
