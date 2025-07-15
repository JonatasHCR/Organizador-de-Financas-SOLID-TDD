from fastapi import FastAPI
from contextlib import asynccontextmanager

from app.core.database import engine, Base
from app.api.version_1.endpoints.conta import router_conta
from app.api.version_1.endpoints.ativo import router_ativo
from app.api.version_1.endpoints.passivo import router_passivo
from app.api.version_1.endpoints.investimento import router_investimento


@asynccontextmanager
async def lifespan(app: FastAPI):
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    yield
    await engine.dispose()


app = FastAPI(
    lifespan=lifespan,
    openapi_tags=[
        {"name": "Ativo", "description": "Operações com Ativos"},
        {"name": "Passivo", "description": "Operações com Passivos"},
        {"name": "Investimento", "description": "Operações com Investimentos"},
        {"name": "conta", "description": "Operações com Contas"},
    ],
)

app.include_router(router_conta)
app.include_router(router_ativo)
app.include_router(router_passivo)
app.include_router(router_investimento)
