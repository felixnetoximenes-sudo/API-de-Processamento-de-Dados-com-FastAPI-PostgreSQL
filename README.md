# 🚀 API de Processamento de Dados com FastAPI & PostgreSQL

Este projeto consiste em uma API robusta de Back-End desenvolvida em Python utilizando o framework **FastAPI** integrado ao banco de dados objeto-relacional **PostgreSQL**. A aplicação valida dados numéricos na entrada e gerencia o ciclo completo de persistência (salvamento e leitura) de informações.

---

## 🛠️ Tecnologias e Ferramentas Utilizadas

*   **Python 3.12+**: Linguagem base do projeto.
*   **FastAPI**: Framework web moderno, de alta performance e com suporte nativo a operações assíncronas.
*   **Pydantic**: Biblioteca para validação de dados e gerenciamento de configurações usando tipos de dados do Python.
*   **PostgreSQL**: Banco de dados relacional escolhido pela sua estabilidade, robustez e conformidade ACID.
*   **Psycopg2-Binary**: Driver de conexão que realiza a ponte de comunicação de baixa latência entre o código Python e o servidor Postgres.
*   **Uvicorn**: Servidor ASGI de alta velocidade para rodar a aplicação.

---

## 💡 Diferenciais Técnicos do Projeto

1.  **Validação Rígida no Schema (Camada Antifalhas):** Utilização do `BaseModel` e do `Field(ge=10)` do Pydantic. Se um usuário tentar enviar um número menor que 10, o FastAPI bloqueia a requisição imediatamente na porta de entrada, poupando processamento e conexões desnecessárias com o banco de dados.
2.  **Arquitetura CRUD de Persistência Real:** Diferente de projetos acadêmicos que salvam dados na memória volátil (que somem ao reiniciar), este sistema se conecta a uma instância real de banco de dados e executa comandos SQL estruturados (`INSERT` e `SELECT`).
3.  **Tratamento de Exceções (Tratamento de Erros 500/422):** Implementação de blocos `try/except` para capturar falhas de infraestrutura e retornar respostas limpas e padronizadas no formato JSON para o cliente.

---

## 🎯 Rotas da API

A API conta com documentação interativa automática gerada pelo Swagger UI.

*   `POST /item`: Recebe um JSON contendo um número inteiro, valida as regras de negócio e realiza um `INSERT` na tabela do PostgreSQL.
*   `GET /itens`: Abre uma conexão de leitura, executa um `SELECT` ordenado de forma decrescente (`ORDER BY id DESC`) e lista todos os registros salvos diretamente na tela.

---

## 🚀 Como Executar o Projeto Localmente

### 1. Clonar o repositório
```bash
git clone https://github.com
cd NOME_DO_REPOSITORIO
```

### 2. Instalar as dependências
```bash
pip install fastapi uvicorn pydantic psycopg2-binary
```

### 3. Configurar o Banco de Dados
Certifique-se de possuir o PostgreSQL rodando localmente com um banco de dados chamado `usuario` e uma tabela estruturada da seguinte forma:
```sql
CREATE TABLE dados (
    id SERIAL PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    criado_em TIMESTAMP DEFAULT NOW()
);
```

### 4. Inicializar o servidor
```bash
python -m uvicorn api:app --reload
```

Acesse a documentação interativa em: `http://127.0.0` para testar os endpoints em tempo real.
