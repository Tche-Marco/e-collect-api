from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
import os

from sqlalchemy.ext.declarative import declarative_base

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

# Cria uma sessão do SQLAlchemy
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
