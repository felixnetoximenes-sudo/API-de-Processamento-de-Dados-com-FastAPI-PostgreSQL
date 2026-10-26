from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
import psycopg2
import requests
class Model(BaseModel):
    numero: int = Field(
    ...,
    description='Digite numeros',
    ge=10
    )
def conectar_banco():
    return psycopg2.connect(
        host="localhost",
        database="usuario",   
        user="postgres",        
        password="123456"    
    )

app = FastAPI(title='Minha api de IA')


@app.post('/item')
def dados (item:Model):
    return {
            'Mensagem': 'Dados Recebidos e salvos no PostgreSQL!',
            'numero_validado': item.numero
        }

# Mantenha todo o seu código anterior aqui em cima...

# Nova rota GET para listar os dados
@app.get('/itens')
def listar_dados():
    try:
        # 1. Abre a conexão com o banco
        conexao = conectar_banco()
        cursor = conexao.cursor()
        
        # 2. Executa o comando SQL para buscar tudo
        sql = "SELECT id, nome, email, criado_em FROM dados ORDER BY id DESC;"
        cursor.execute(sql)
        
        # 3. Puxa todos os registros encontrados no banco
        linhas = cursor.fetchall()
        
        # 4. Fecha as conexões
        cursor.close()
        conexao.close()
        
        # 5. Organiza os dados em um formato bonito (JSON) para enviar à API
        lista_usuarios = []
        for linha in linhas:
            lista_usuarios.append({
                "id": linha[0],
                "nome": linha[1],
                "email": linha[2],
                "criado_em": str(linha[3]) # Transforma a data em texto para não dar erro
            })
            
        return {
            "total_registros": len(lista_usuarios),
            "usuarios_salvos": lista_usuarios
        }
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erro ao buscar no banco: {str(e)}")
