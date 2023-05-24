import os

from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

load_dotenv()  # Carrega as variáveis de ambiente do arquivo .env

# Obtém as variáveis de ambiente
db_user = os.getenv("DB_USER")
db_password = os.getenv("DB_PASSWORD")
db_host = os.getenv("DB_HOST")
db_name = os.getenv("DB_NAME")

# Constrói a URL de conexão com o banco de dados
db_url = f"postgresql://{db_user}:{db_password}@{db_host}/{db_name}"

# Cria a engine do SQLAlchemy
engine = create_engine(db_url)

# Cria uma sessão do SQLAlchemy.
# A sessão é a principal interface do usuário para persistir e selecionar objetos a partir do banco de dados.
# Ela é configurada com o parâmetro 'autocommit' como False para que possamos controlar a transação explicitamente.
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Cria a base declarativa para os modelos do SQLAlchemy.
Base = declarative_base()


def get_db():
    """
    Função para obter uma sessão de banco de dados.
    Ela cria uma sessão local, fornece ao chamador, e então fecha a sessão (mesmo que haja uma exceção).
    É utilizada com o gerenciador de contexto do Python (palavra-chave 'with').
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
