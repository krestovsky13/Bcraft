import datetime
from decimal import Decimal
from typing import Optional, Any
from pydantic import BaseModel, Field, validator
from pydantic.types import StrictInt, NonNegativeInt


# class RestrictedAlphabetStr(float):
#     # @classmethod
#     # def __get_validators__(cls) -> Generator[Callable, None, None]:
#     #     yield cls.validate
#     #
#     # @classmethod
#     # def validate(cls, value: str, field: ModelField):
#     #     alphabet = field.field_info.extra['alphabet']
#     #     if any(c not in alphabet for c in value):
#     #         raise ValueError(f'{value!r} is not restricted to {alphabet!r}')
#     #     return cls(value)
#
#     @classmethod
#     def __modify_schema__(
#         cls, field_schema: dict[str, Any], field: type['Statistic'] | None
#     ):
#         if field:
#             ...

#
# class MyModel(BaseModel):
#     value: RestrictedAlphabetStr = Field(alphabet='ABC')

class PositiveStrictInt(StrictInt, NonNegativeInt):
    """
    Валидация не отрицательного целого числа
    """
    pass


class CreateStatistic(BaseModel):
    """
    Схема создания записи
    """
    date: datetime.date
    views: Optional[PositiveStrictInt] = 0
    clicks: Optional[PositiveStrictInt] = 0
    cost: Optional[Decimal] = Field(default=0, decimal_places=2, ge=0)

    class Config:
        orm_mode = True


class ShowPeriodStatistic(BaseModel):
    """
    Схема просмотра записей за выбранный период
    """
    from_field: datetime.date = Field(..., alias='from')
    to: datetime.date


class ShowStatistic(CreateStatistic):
    """
    Схема просмотра записи
    """
    cpc: Decimal = Field(default=0, decimal_places=2)
    cpm: Decimal = Field(default=0, decimal_places=2)

    @validator('cpc', always=True)
    def a(cls, v, values) -> Decimal | int:
        """
        Serializermethodfield
        """
        return round(values['cost'] / values['clicks'], 2) if values['clicks'] else 0

    @validator('cpm', always=True)
    def b(cls, v, values) -> Decimal | int:
        """
        Serializermethodfield
        """
        return round(values['cost'] / values['views'], 2) * 1000 if values['views'] else 0
