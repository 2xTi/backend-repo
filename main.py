from fastapi import FastAPI
from fastapi.params import Body
import classes

app = FastAPI()

    
@app.get ("/")
def read_root():
    return {"Hello": "lala"}

@app.post("/criar")
def criar_valores(nova_mensagem: classes.Mensagem):
    print(nova_mensagem)
    return {"Mensagem": f"Titulo: {nova_mensagem.titulo} Mensagem: {nova_mensagem.conteudo} Publicada: {nova_mensagem.publicada}"}

@app.post("/criar")
def criar_valores(res: dict = Body(...)):
    print(res)
    return {"Mensagem": "Criado com Sucesso!"}

@app.post("/criar")
def criar_valores(res: dict = Body(...)):
    print(res)
    return {"Mensagem": f"lala: {res['lala']} lele: {res['lele']}"}