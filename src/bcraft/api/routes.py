from typing import Optional

from fastapi import APIRouter, Depends
from starlette import status

from bcraft.api.deps import get_repository, validate_query_params
from bcraft.api.schemas import CreateStatistic, ShowPeriodStatistic, ShowStatistic
from bcraft.api.services import StatisticRepository

router = APIRouter(
    prefix='/statistic',
    tags=['statistic'],
)


@router.post("/save", response_model=CreateStatistic, status_code=status.HTTP_200_OK)
async def save_stats(
        stats_schema: CreateStatistic,
        stats_services: StatisticRepository = Depends(get_repository(StatisticRepository)),
):
    return await stats_services.create_or_update(stats_schema)


@router.post("/show", response_model=list[ShowStatistic], status_code=status.HTTP_200_OK)
async def show_stats(
        stats_schema: ShowPeriodStatistic,
        stats_services: StatisticRepository = Depends(get_repository(StatisticRepository)),
        sort_by: Optional[str] = Depends(validate_query_params),
        order_by: Optional[str] = Depends(validate_query_params),
):
    return await stats_services.get_stats_for_period(stats_schema, sort_by, order_by)


@router.delete("/reset", status_code=status.HTTP_200_OK)
async def reset_stats(stats_services: StatisticRepository = Depends(get_repository(StatisticRepository))):
    await stats_services.clear_all_stats()
    return {"msg": "Statistics cleared successfully"}
