from typing import Literal, Optional
from pydantic import Field

from app.schema.base import BaseSchema


class PassivoSchema(BaseSchema):

    frequencia: Optional[Literal["D", "M", "S"]]


class PassivoOutputSchema(PassivoSchema):

    id: int = Field(..., gt=0)
