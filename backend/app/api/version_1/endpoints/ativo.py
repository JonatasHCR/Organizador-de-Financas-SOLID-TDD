from typing import List

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


@router_ativo.put("/update/{ativo_id}", response_model=AtivoResponseSchema)
async def update_ativo(
    ativo_id: int, ativo_schema: AtivoSchema, db: AsyncSession = Depends(get_db)
):
    service = AtivoService(db)
    try:
        return await service.update(ativo_id, ativo_schema)
    except ValueError as error:
        raise HTTPException(status_code=400, detail=str(error))


@router_ativo.delete("/delete/{ativo_id}", response_model=AtivoResponseSchema)
async def delete_ativo(ativo_id: int, db: AsyncSession = Depends(get_db)):
    service = AtivoService(db)
    try:
        return await service.delete(ativo_id)
    except ValueError as error:
        raise HTTPException(status_code=400, detail=str(error))


@router_ativo.get("/{ativo_id}", response_model=AtivoOutputSchema)
async def get_ativo_by_id(ativo_id: int, db: AsyncSession = Depends(get_db)):
    service = AtivoService(db)
    try:
        return await service.get_by_id(ativo_id)
    except ValueError as error:
        raise HTTPException(status_code=400, detail=str(error))


@router_ativo.get("/conta/id/{conta_id}", response_model=List[AtivoOutputSchema])
async def get_ativo_by_conta_id(
    conta_id: int, db: AsyncSession = Depends(get_db)
) -> list[AtivoOutputSchema]:
    service = AtivoService(db)
    try:
        return await service.get_by_conta_id(conta_id)
    except ValueError as error:
        raise HTTPException(status_code=400, detail=str(error))


@router_ativo.get("/eh/fixo", response_model=List[AtivoOutputSchema])
async def get_ativo_eh_fixo(
    eh_fixo: bool, db: AsyncSession = Depends(get_db)
) -> list[AtivoOutputSchema]:
    service = AtivoService(db)
    try:
        return await service.get_eh_fixo(eh_fixo)
    except ValueError as error:
        raise HTTPException(status_code=400, detail=str(error))


@router_ativo.get(
    "/remuneracao/{tipo_remuneracao}", response_model=List[AtivoOutputSchema]
)
async def get_ativo_by_tipo_remuneracao(
    tipo_remuneracao: str, db: AsyncSession = Depends(get_db)
) -> list[AtivoOutputSchema]:
    service = AtivoService(db)
    try:
        return await service.get_by_tipo_remuneracao(tipo_remuneracao)
    except ValueError as error:
        raise HTTPException(status_code=400, detail=str(error))


@router_ativo.get("/referencia/{referencia}", response_model=List[AtivoOutputSchema])
async def get_ativo_by_referencia(
    referencia: str, db: AsyncSession = Depends(get_db)
) -> list[AtivoOutputSchema]:
    service = AtivoService(db)
    try:
        return await service.get_by_referencia(referencia)
    except ValueError as error:
        raise HTTPException(status_code=400, detail=str(error))


@router_ativo.get("/", response_model=List[AtivoOutputSchema])
async def get_ativo_all(db: AsyncSession = Depends(get_db)) -> list[AtivoOutputSchema]:
    service = AtivoService(db)
    try:
        return await service.get_all()
    except ValueError as error:
        raise HTTPException(status_code=400, detail=str(error))
