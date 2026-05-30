from fastapi import APIRouter, Depends
from typing import List
from src.schemas.account import AccountIn
from src.views.account import AccountOut
from src.views.transaction import TransactionOut
from src.services.account import AccountService
from src.services.transaction import TransactionService
from src.security import login_required

router = APIRouter(prefix="/accounts", dependencies=[Depends(login_required)])
account_service = AccountService()
tx_service = TransactionService()

@router.get("/", response_model=List[AccountOut], summary="Listar todas as contas")
async def read_accounts(limit: int = 5, skip: int = 0):
    return await account_service.read_all(limit=limit, skip=skip)

@router.post("/", response_model=AccountOut, summary="Criar nova conta corrente")
async def create_account(account: AccountIn):
    return await account_service.create(account)

@router.get("/{id}/transactions", response_model=List[TransactionOut], summary="Visualizar extrato da conta")
async def read_account_transactions(id: int, limit: int = 5, skip: int = 0):
    return await tx_service.read_all(account_id=id, limit=limit, skip=skip)
