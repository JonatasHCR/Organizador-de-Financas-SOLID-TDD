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
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
