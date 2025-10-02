from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.version_1.endpoints.conta import ContaEndpoint
from app.api.version_1.endpoints.ativo import AtivoEndpoint
from app.api.version_1.endpoints.passivo import PassivoEndpoint


app = FastAPI(
    title="Organizador de Finanças API",
    docs_url="/documentation",
    redoc_url="/recaudacao",
    openapi_url="/api/openapi.json",
    openapi_tags=[
        {"name": "Conta", "description": "Operações com Contas"},
        {"name": "Ativo", "description": "Operações com Ativos"},
        {"name": "Passivo", "description": "Operações com Passivos"},
        {"name": "Investimento", "description": "Operações com Investimentos"},
    ],
)

origins = [
    "http://localhost",
    "http://localhost:9002",
    "http://localhost:3000",
    "http://127.0.0.1",
    "http://127.0.0.1:9002",
    "http://127.0.0.1:3000",
    "http://10.0.0.199",
    "http://10.0.0.199:9002",
    "http://10.0.0.199:3000",
]


app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(ContaEndpoint().router)
app.include_router(AtivoEndpoint().router)
app.include_router(PassivoEndpoint().router)
