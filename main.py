import uvicorn
from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from app.core.database import Base, engine
from app.core.routes import api_router


app = FastAPI()


@app.get("/", include_in_schema=False)
def read_root():
    """
    Redireciona as requisições da raiz ("/") para a documentação do Swagger UI em "/docs".

    Returns:
        response: A instância do RedirectResponse apontando para "/docs".
    """
    response = RedirectResponse(url="/docs")
    return response


def create_tables():
    """
    Cria todas as tabelas definidas na base do SQLAlchemy (instanciada como Base).
    """
    Base.metadata.create_all(bind=engine)


def startup():
    """
    Função de inicialização para criar tabelas no banco de dados quando a aplicação é iniciada.
    """
    create_tables()


app.add_event_handler("startup", startup)

app.include_router(api_router)

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
