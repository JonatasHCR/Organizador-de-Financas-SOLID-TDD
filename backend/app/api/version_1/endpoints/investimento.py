from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.database import get_db
from app.schema.investimento import (
    InvestimentoSchema,
    InvestimentoOutputSchema,
    InvestimentoResponseSchema,
)
from app.service.investimento import InvestimentoService


router_investimento = APIRouter(prefix="/investimento", tags=["Investimento"])


@router_investimento.post("/create", response_model=InvestimentoResponseSchema)
async def create_investimento(
    investimento_schema: InvestimentoSchema, db: AsyncSession = Depends(get_db)
):
    service = InvestimentoService(db)
    try:
        return await service.create(investimento_schema)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
