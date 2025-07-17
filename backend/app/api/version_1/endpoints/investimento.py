from typing import List

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


@router_investimento.put(
    "/update/{investimento_id}", response_model=InvestimentoResponseSchema
)
async def update_investimento(
    investimento_id: int,
    investimento_schema: InvestimentoSchema,
    db: AsyncSession = Depends(get_db),
):
    service = InvestimentoService(db)
    try:
        return await service.update(investimento_id, investimento_schema)
    except ValueError as error:
        raise HTTPException(status_code=400, detail=str(error))


@router_investimento.delete(
    "/delete/{investimento_id}", response_model=InvestimentoResponseSchema
)
async def delete_investimento(investimento_id: int, db: AsyncSession = Depends(get_db)):
    service = InvestimentoService(db)
    try:
        return await service.delete(investimento_id)
    except ValueError as error:
        raise HTTPException(status_code=400, detail=str(error))


@router_investimento.get("/{investimento_id}", response_model=InvestimentoOutputSchema)
async def get_investimento_by_id(
    investimento_id: int, db: AsyncSession = Depends(get_db)
):
    service = InvestimentoService(db)
    try:
        return await service.get_by_id(investimento_id)
    except ValueError as error:
        raise HTTPException(status_code=400, detail=str(error))


@router_investimento.get("/", response_model=List[InvestimentoOutputSchema])
async def get_investimento_all(
    db: AsyncSession = Depends(get_db),
) -> list[InvestimentoOutputSchema]:
    service = InvestimentoService(db)
    try:
        return await service.get_all()
    except ValueError as error:
        raise HTTPException(status_code=400, detail=str(error))


@router_investimento.get(
    "/conta/id/{conta_id}", response_model=List[InvestimentoOutputSchema]
)
async def get_investimento_by_conta_id(
    conta_id: int, db: AsyncSession = Depends(get_db)
) -> list[InvestimentoOutputSchema]:
    service = InvestimentoService(db)
    try:
        return await service.get_by_conta(conta_id)
    except ValueError as error:
        raise HTTPException(status_code=400, detail=str(error))
