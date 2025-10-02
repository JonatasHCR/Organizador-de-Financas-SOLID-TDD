from typing import List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.database import get_db
from app.schema.ativo import AtivoSchema, AtivoOutputSchema
from app.service.ativo import AtivoService


class AtivoEndpoint:
    def __init__(self):
        self.service = AtivoService
        self.router = APIRouter(prefix="/ativos", tags=["Ativo"])

        self.register_routes()

    def register_routes(self):
        self.router.post("/", response_model=AtivoOutputSchema, status_code=201)(
            self._create
        )
        self.router.put("/{id}", response_model=AtivoOutputSchema, status_code=200)(
            self._update
        )
        self.router.delete("/{id}", response_model=None, status_code=204)(self._delete)

        self.router.get("/", response_model=list[AtivoOutputSchema])(self._get_all)
        self.router.get("/{id}", response_model=AtivoOutputSchema)(self._get_by_id)
        self.router.get("/conta/{user_id}", response_model=list[AtivoOutputSchema])(
            self.get_by_conta_id
        )
        self.router.get("/fixo", response_model=List[AtivoOutputSchema])(
            self.get_by_fixo
        )
        self.router.get(
            "/frequencia/{frequencia}", response_model=List[AtivoOutputSchema]
        )(self.get_by_frequencia)
        self.router.get(
            "/referencia/{referencia}", response_model=List[AtivoOutputSchema]
        )(self.get_by_referencia)

    async def _get_by_id(
        self, id: int, db: AsyncSession = Depends(get_db)
    ) -> AtivoOutputSchema:
        service = self.service(db)
        try:
            return await service.get_by_id(id)
        except ValueError as error:
            raise HTTPException(
                status_code=404,
                detail=str(error).format(id=id, objeto="Ativo"),
            )

    async def _get_all(
        self, limit: int = 100, offset: int = 0, db: AsyncSession = Depends(get_db)
    ) -> list[AtivoOutputSchema]:
        service = self.service(db)
        return await service.get_all(limit=limit, offset=offset)

    async def _create(
        self, schema: AtivoSchema, db: AsyncSession = Depends(get_db)
    ) -> AtivoOutputSchema:
        service = self.service(db)

        return await service.create(schema)

    async def _update(
        self, id: int, schema: AtivoSchema, db: AsyncSession = Depends(get_db)
    ) -> AtivoOutputSchema:
        service = self.service(db)
        try:
            return await service.update(id, schema)
        except ValueError as error:
            raise HTTPException(
                status_code=404,
                detail=str(error).format(id=id, objeto="Ativo"),
            )

    async def _delete(self, id: int, db: AsyncSession = Depends(get_db)) -> None:
        service = self.service(db)
        try:
            return await service.delete(id)
        except ValueError as error:
            raise HTTPException(
                status_code=404,
                detail=str(error).format(id=id, objeto="Ativo"),
            )

    async def get_by_conta_id(
        self, conta_id: int, db: AsyncSession = Depends(get_db)
    ) -> list[AtivoOutputSchema]:
        service = self.service(db)
        try:
            return await service.get_by_conta_id(conta_id)
        except ValueError as error:
            raise HTTPException(status_code=400, detail=str(error))

    async def get_by_fixo(
        self, fixo: bool, db: AsyncSession = Depends(get_db)
    ) -> list[AtivoOutputSchema]:
        service = self.service(db)
        try:
            return await service.get_by_fixo(fixo)
        except ValueError as error:
            raise HTTPException(status_code=400, detail=str(error))

    async def get_by_frequencia(
        self, frequencia: str, db: AsyncSession = Depends(get_db)
    ) -> list[AtivoOutputSchema]:
        service = self.service(db)
        try:
            return await service.get_by_frequencia(frequencia)
        except ValueError as error:
            raise HTTPException(status_code=400, detail=str(error))

    async def get_by_referencia(
        self, referencia: str, db: AsyncSession = Depends(get_db)
    ) -> list[AtivoOutputSchema]:
        service = self.service(db)
        try:
            return await service.get_by_referencia(referencia)
        except ValueError as error:
            raise HTTPException(status_code=400, detail=str(error))
