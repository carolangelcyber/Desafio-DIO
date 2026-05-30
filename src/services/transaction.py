from typing import List
from src.database import database
from src.models.transaction import transactions, TransactionType
from src.models.account import accounts
from src.schemas.transaction import TransactionIn
from src.exceptions import AccountNotFoundError, BusinessError

class TransactionService:
    async def read_all(self, account_id: int, limit: int, skip: int = 0) -> List[dict]:
        query = transactions.select().where(transactions.c.account_id == account_id).limit(limit).offset(skip)
        return await database.fetch_all(query)

    @database.transaction()
    async def create(self, transaction: TransactionIn) -> dict:
        query_account = accounts.select().where(accounts.c.id == transaction.account_id)
        account = await database.fetch_one(query_account)
        
        if not account:
            raise AccountNotFoundError()
            
        current_balance = account["balance"]
        
        # Validação do requisito de negócio: Bloquear saques sem saldo suficiente
        if transaction.type == TransactionType.WITHDRAWAL:
            if current_balance < transaction.amount:
                raise BusinessError("Saldo insuficiente para realizar esta operação de saque.")
            new_balance = current_balance - transaction.amount
        else:
            new_balance = current_balance + transaction.amount

        await self._update_account_balance(transaction.account_id, new_balance)
        tx_id = await self._register_transaction(transaction)
        
        query_tx = transactions.select().where(transactions.c.id == tx_id)
        return await database.fetch_one(query_tx)

    async def _update_account_balance(self, account_id: int, balance: float) -> None:
        command = accounts.update().where(accounts.c.id == account_id).values(balance=balance)
        await database.execute(command)

    async def _register_transaction(self, transaction: TransactionIn) -> int:
        command = transactions.insert().values(
            account_id=transaction.account_id,
            type=transaction.type,
            amount=transaction.amount
        )
        return await database.execute(command)
