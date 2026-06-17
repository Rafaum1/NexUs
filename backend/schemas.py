from pydantic import BaseModel

class UsuarioCreate(BaseModel):
    nome: str
    email: str
    senha: str

class UsuarioResponse(BaseModel):
    id: int
    nome: str
    email: str
    tipo: str
    ativo: bool

    class Config:
        from_attributes = True

class LoginRequest(BaseModel):
    email: str
    senha: str
