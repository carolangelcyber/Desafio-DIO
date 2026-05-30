import enum
import sqlalchemy as sa
from src.models.account import metadata, accounts

# Enum para os tipos de transações aceitas na API Bancária
class TransactionType(str, enum.Enum):
    DEPOSIT = "deposito"
    WITHDRAWAL = "saque"

# Definição assíncrona da tabela de transações históricas
transactions = sa.Table(
    "transactions",
    metadata,
    sa.Column("id", sa.Integer, primary_key=True, autoincrement=True),
    sa.Column("account_id", sa.Integer, sa.ForeignKey("accounts.id"), nullable=False),
    sa.Column("type", sa.Enum(TransactionType), nullable=False),
    sa.Column("amount", sa.Numeric(10, 2), nullable=False),
    sa.Column("timestamp", sa.DateTime, server_default=sa.func.now(), nullable=False),
)
