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


@router_conta.put("/update/{conta_id}", response_model=ContaResponseSchema)
async def update_conta(
    conta_id: int, conta_schema: ContaSchema, db: AsyncSession = Depends(get_db)
):
    service = ContaService(db)
    try:
        return await service.update(conta_id, conta_schema)
    except ValueError as error:
        raise HTTPException(status_code=400, detail=str(error))


@router_conta.delete("/delete/{conta_id}", response_model=ContaResponseSchema)
async def delete_conta(conta_id: int, db: AsyncSession = Depends(get_db)):
    service = ContaService(db)
    try:
        return await service.delete(conta_id)
    except ValueError as error:
        raise HTTPException(status_code=400, detail=str(error))


@router_conta.get("/{conta_id}", response_model=ContaOutputSchema)
async def get_conta_by_id(conta_id: int, db: AsyncSession = Depends(get_db)):
    service = ContaService(db)
    try:
        return await service.get_by_id(conta_id)
    except ValueError as error:
        raise HTTPException(status_code=400, detail=str(error))
