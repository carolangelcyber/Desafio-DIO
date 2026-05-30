from pydantic import BaseModel, PositiveFloat

# Esquema para validação de entrada ao criar uma conta
class AccountIn(BaseModel):
    user_id: int
    balance: PositiveFloat # Garante saldo inicial maior que zero
