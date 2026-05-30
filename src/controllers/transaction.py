from fastapi import APIRouter, Depends
from src.schemas.transaction import TransactionIn
from src.views.transaction import TransactionOut
from src.services.transaction import TransactionService
from src.security import login_required

router = APIRouter(prefix="/transactions", dependencies=[Depends(login_required)])
service = TransactionService()

@router.post("/", response_model=TransactionOut, summary="Cadastrar transação (Depósito/Saque)")
async def create_transaction(transaction: TransactionIn):
    return await service.create(transaction)
