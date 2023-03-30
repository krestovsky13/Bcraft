from typing import Type

from sqlalchemy import text, desc, asc, func
from sqlalchemy.orm import Session

from bcraft.api.models import Statistic
from bcraft.api.schemas import CreateStatistic, ShowPeriodStatistic
from bcraft.repository import BaseRepository


class StatisticRepository(BaseRepository):
    """"
    Класс операций в БД для модели статистики
    """
    def __init__(self, session: Session):
        self.model = Statistic
        super().__init__(session=session)

    async def create_or_update(self, obj: CreateStatistic) -> Type[Statistic]:
        """
        Создаем запись или агрегируем при наличии
        """
        obj = self.model(**obj.dict())
        if existing_obj := self.session.query(self.model).filter(self.model.date == obj.date).one_or_none():
            existing_obj.views += obj.views
            existing_obj.clicks += obj.clicks
            existing_obj.cost += obj.cost
        else:
            self.session.add(obj)
        self.commit()

        return existing_obj or obj

    async def get_stats_for_period(self, time_frame: ShowPeriodStatistic, *args) -> list[Type[Statistic]]:
        """
        Получаем всю статистика за период
        """
        self.session.query(
            self.model.clicks,
            func.avg(self.model.clicks).label('rating'),
            func.count('*').label('review_count'),
        )

        field = args[0][0]
        sort = asc if (args[1][1] == 'asc') else desc

        period = time_frame.dict()
        return self.session.query(self.model).filter(
            self.model.date >= period['from_field'],
            self.model.date <= period['to'],
        ).order_by(sort(field)).all()

    async def clear_all_stats(self):
        """
        Сбрасываем всю статистику
        """
        sql = text(f'TRUNCATE {self.model.__tablename__} RESTART IDENTITY')
        self.session.execute(sql)
        self.commit()
