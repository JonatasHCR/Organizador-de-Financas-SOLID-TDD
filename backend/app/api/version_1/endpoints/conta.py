from typing import List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.database import get_db
from app.schema.conta import ContaSchema, ContaOutputSchema
from app.service.conta import ContaService


class ContaEndpoint:
    def __init__(self):
        self.service = ContaService
        self.router = APIRouter(prefix="/contas", tags=["Conta"])

        self.register_routes()

    def register_routes(self):
        self.router.post("/", response_model=ContaOutputSchema, status_code=201)(
            self._create
        )
        self.router.put("/{id}", response_model=ContaOutputSchema, status_code=200)(
            self._update
        )
        self.router.delete("/{id}", response_model=None, status_code=204)(self._delete)

        self.router.get("/", response_model=list[ContaOutputSchema])(self._get_all)
        self.router.get("/{id}", response_model=ContaOutputSchema)(self._get_by_id)
        self.router.get("/nome/{nome}", response_model=list[ContaOutputSchema])(
            self.get_by_nome
        )

    async def _get_by_id(
        self, id: int, db: AsyncSession = Depends(get_db)
    ) -> ContaOutputSchema:
        service = self.service(db)
        try:
            return await service.get_by_id(id)
        except ValueError as error:
            raise HTTPException(
                status_code=404,
                detail=str(error).format(id=id, objeto="Conta"),
            )

    async def _get_all(
        self, limit: int = 100, offset: int = 0, db: AsyncSession = Depends(get_db)
    ) -> list[ContaOutputSchema]:
        service = self.service(db)
        return await service.get_all(limit=limit, offset=offset)

    async def _create(
        self, schema: ContaSchema, db: AsyncSession = Depends(get_db)
    ) -> ContaOutputSchema:
        service = self.service(db)

        return await service.create(schema)

    async def _update(
        self, id: int, schema: ContaSchema, db: AsyncSession = Depends(get_db)
    ) -> ContaOutputSchema:
        service = self.service(db)
        try:
            return await service.update(id, schema)
        except ValueError as error:
            raise HTTPException(
                status_code=404,
                detail=str(error).format(id=id, objeto="Conta"),
            )

    async def _delete(self, id: int, db: AsyncSession = Depends(get_db)) -> None:
        service = self.service(db)
        try:
            return await service.delete(id)
        except ValueError as error:
            raise HTTPException(
                status_code=404,
                detail=str(error).format(id=id, objeto="Conta"),
            )

    async def get_by_nome(
        self, nome: str, db: AsyncSession = Depends(get_db)
    ) -> list[ContaOutputSchema]:
        service = self.service(db)
        try:
            return await service.get_by_nome(nome)
        except ValueError as error:
            raise HTTPException(status_code=404, detail=str(error))
