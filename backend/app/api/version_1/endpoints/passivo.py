from typing import List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.database import get_db
from app.schema.passivo import PassivoSchema, PassivoOutputSchema, PassivoResponseSchema
from app.service.passivo import PassivoService


router_passivo = APIRouter(prefix="/passivo", tags=["Passivo"])


@router_passivo.post("/create", response_model=PassivoResponseSchema)
async def create_passivo(
    passivo_schema: PassivoSchema, db: AsyncSession = Depends(get_db)
):
    service = PassivoService(db)
    try:
        return await service.create(passivo_schema)
    except ValueError as error:
        raise HTTPException(status_code=400, detail=str(error))


@router_passivo.put("/update/{passivo_id}", response_model=PassivoResponseSchema)
async def update_passivo(
    passivo_id: int, passivo_schema: PassivoSchema, db: AsyncSession = Depends(get_db)
):
    service = PassivoService(db)
    try:
        return await service.update(passivo_id, passivo_schema)
    except ValueError as error:
        raise HTTPException(status_code=400, detail=str(error))


@router_passivo.delete("/delete/{passivo_id}", response_model=PassivoResponseSchema)
async def delete_passivo(passivo_id: int, db: AsyncSession = Depends(get_db)):
    service = PassivoService(db)
    try:
        return await service.delete(passivo_id)
    except ValueError as error:
        raise HTTPException(status_code=400, detail=str(error))


@router_passivo.get("/{passivo_id}", response_model=PassivoOutputSchema)
async def get_passivo_by_id(passivo_id: int, db: AsyncSession = Depends(get_db)):
    service = PassivoService(db)
    try:
        return await service.get_by_id(passivo_id)
    except ValueError as error:
        raise HTTPException(status_code=400, detail=str(error))


@router_passivo.get("/", response_model=List[PassivoOutputSchema])
async def get_passivo_all(
    db: AsyncSession = Depends(get_db),
) -> list[PassivoOutputSchema]:
    service = PassivoService(db)
    try:
        return await service.get_all()
    except ValueError as error:
        raise HTTPException(status_code=400, detail=str(error))


@router_passivo.get("/conta/id/{conta_id}", response_model=List[PassivoOutputSchema])
async def get_passivo_by_conta_id(
    conta_id: int, db: AsyncSession = Depends(get_db)
) -> list[PassivoOutputSchema]:
    service = PassivoService(db)
    try:
        return await service.get_by_conta_id(conta_id)
    except ValueError as error:
        raise HTTPException(status_code=400, detail=str(error))
