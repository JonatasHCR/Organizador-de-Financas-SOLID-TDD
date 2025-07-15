from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.database import get_db
from app.schema.ativo import AtivoSchema, AtivoOutputSchema, AtivoResponseSchema
from app.service.ativo import AtivoService


router_ativo = APIRouter(prefix="/ativo", tags=["Ativo"])


@router_ativo.post("/create", response_model=AtivoResponseSchema)
async def create_ativo(ativo_schema: AtivoSchema, db: AsyncSession = Depends(get_db)):
    service = AtivoService(db)
    try:
        return await service.create(ativo_schema)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
