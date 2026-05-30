from pydantic import BaseModel

# Estrutura de retorno após um login realizado com sucesso
class LoginOut(BaseModel):
    access_token: str
