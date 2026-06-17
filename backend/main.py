from fastapi import FastAPI
from database import engine, Base, SessionLocal
from models import Usuario
from schemas import UsuarioCreate, UsuarioResponse
from security import gerar_hash

Base.metadata.create_all(bind=engine)
app = FastAPI()

@app.get("/")
def home():
    return {
        "sistema": "NexUs",
        "status": "online"
    }

@app.post("/usuarios")
def criar_usuario(usuario: UsuarioCreate):

    db = SessionLocal()
    novo_usuario = Usuario(
        nome=usuario.nome,
        email=usuario.email,
        senha_hash=gerar_hash(usuario.senha),
        tipo="usuario"
    )

    db.add(novo_usuario)
    db.commit()
    db.refresh(novo_usuario)
    db.close()

    return{
        "id": novo_usuario.id,
        "nome": novo_usuario.nome,
        "email": novo_usuario.email
    }

@app.get("/usuarios", response_model=list[UsuarioResponse])
def listar_usuarios():
    db = SessionLocal()
    usuarios = db.query(Usuario).all()
    db.close()
    return usuarios

@app.get("/usuarios/{id}", response_model=UsuarioResponse)
def listar_usuarios_id(id: int):
    db = SessionLocal()
    usuarios = db.query(Usuario).filter(Usuario.id == id).first()
    db.close()
    return usuarios