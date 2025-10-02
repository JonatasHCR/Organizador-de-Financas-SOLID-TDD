from typing import Optional, Literal
from pydantic import Field

from app.schema.base import BaseSchema


class AtivoSchema(BaseSchema):

    fequencia: Optional[Literal["Q", "M", "S"]]


class AtivoOutputSchema(AtivoSchema):
    
    id : int = Field(..., gt=0)
