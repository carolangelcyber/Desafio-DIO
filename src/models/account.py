import sqlalchemy as sa

# Inicializa os metadados para mapeamento das tabelas da API Bancária
metadata = sa.MetaData()

# Definição assíncrona da tabela de contas correntes (padrão SQLAlchemy Core)
accounts = sa.Table(
    "accounts",
    metadata,
    sa.Column("id", sa.Integer, primary_key=True, autoincrement=True),
    sa.Column("user_id", sa.Integer, nullable=False),
    sa.Column("balance", sa.Numeric(10, 2), nullable=False, default=0.0),
    sa.Column("created_at", sa.DateTime, server_default=sa.func.now(), nullable=False),
)
