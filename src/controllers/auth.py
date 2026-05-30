from fastapi import APIRouter
from pydantic import BaseModel
from src.views.auth import LoginOut

router = APIRouter(prefix="/auth")

class LoginIn(BaseModel):
    user_id: int

async def sign_jwt(user_id: int) -> str:
    # Simulação simplificada de geração de token JWT mostrada no desafio
    return f"token_assinado_usuario_{user_id}"

@router.post("/login", response_model=LoginOut, summary="Realizar login do usuário")
async def login(data: LoginIn):
    token = await sign_jwt(user_id=data.user_id)
    return {"access_token": token}
