from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.database import get_db
from app.schema.conta import ContaSchema, ContaOutputSchema, ContaResponseSchema
from app.service.conta import ContaService


router_conta = APIRouter(prefix="/conta", tags=["Conta"])


@router_conta.post("/create", response_model=ContaResponseSchema)
async def create_conta(conta_schema: ContaSchema, db: AsyncSession = Depends(get_db)):
    service = ContaService(db)
    try:
        return await service.create(conta_schema)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
