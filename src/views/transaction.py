from pydantic import BaseModel, AwareDatetime, NaiveDatetime, PositiveFloat

# Estrutura de resposta pública para o extrato de transações
class TransactionOut(BaseModel):
    id: int
    account_id: int
    type: str
    amount: PositiveFloat
    timestamp: AwareDatetime | NaiveDatetime
