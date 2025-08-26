from typing import List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.database import get_db
from app.schema.conta import ContaSchema, ContaOutputSchema, ContaResponseSchema
from app.service.conta import ContaService


router_conta = APIRouter(prefix="/contas", tags=["Conta"])


@router_conta.post("/", response_model=ContaResponseSchema, status_code=201)
async def create_conta(
    conta_schema: ContaSchema, db: AsyncSession = Depends(get_db)
) -> ContaResponseSchema:
    service = ContaService(db)
    try:
        return await service.create(conta_schema)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))


@router_conta.put("/{conta_id}", response_model=ContaResponseSchema)
async def update_conta(
    conta_id: int, conta_schema: ContaSchema, db: AsyncSession = Depends(get_db)
) -> ContaResponseSchema:
    service = ContaService(db)
    try:
        return await service.update(conta_id, conta_schema)
    except ValueError as error:
        raise HTTPException(status_code=400, detail=str(error))


@router_conta.delete("/{conta_id}", response_model=ContaResponseSchema)
async def delete_conta(
    conta_id: int, db: AsyncSession = Depends(get_db)
) -> ContaResponseSchema:
    service = ContaService(db)
    try:
        return await service.delete(conta_id)
    except ValueError as error:
        raise HTTPException(status_code=400, detail=str(error))


@router_conta.get("/id/{conta_id}", response_model=ContaOutputSchema)
async def get_conta_by_id(
    conta_id: int, db: AsyncSession = Depends(get_db)
) -> ContaOutputSchema:
    service = ContaService(db)
    try:
        return await service.get_by_id(conta_id)
    except ValueError as error:
        raise HTTPException(status_code=400, detail=str(error))


@router_conta.get("/name/{conta_name}", response_model=ContaOutputSchema)
async def get_conta_by_id(
    conta_name: str, db: AsyncSession = Depends(get_db)
) -> ContaOutputSchema:
    service = ContaService(db)
    try:
        return await service.get_by_nome(conta_name)
    except ValueError as error:
        raise HTTPException(status_code=400, detail=str(error))


@router_conta.get("/", response_model=List[ContaOutputSchema])
async def get_conta_all(db: AsyncSession = Depends(get_db)) -> list[ContaOutputSchema]:
    service = ContaService(db)
    try:
        return await service.get_all()
    except ValueError as error:
        raise HTTPException(status_code=400, detail=str(error))
