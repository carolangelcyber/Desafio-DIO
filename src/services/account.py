from typing import List
from src.database import database
from src.models.account import accounts
from src.schemas.account import AccountIn

class AccountService:
    async def read_all(self, limit: int, skip: int = 0) -> List[dict]:
        query = accounts.select().limit(limit).offset(skip)
        return await database.fetch_all(query)

    async def create(self, account: AccountIn) -> dict:
        command = accounts.insert().values(user_id=account.user_id, balance=account.balance)
        account_id = await database.execute(command)
        
        query = accounts.select().where(accounts.c.id == account_id)
        return await database.fetch_one(query)
