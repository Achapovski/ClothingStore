from decimal import Decimal

from pydantic import BaseModel, Field


class Test(BaseModel):
    number: Decimal = Field()


data = Decimal("2.3")
