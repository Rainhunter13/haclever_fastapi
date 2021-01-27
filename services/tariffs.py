"""Tariffs related services"""

from models import Tariff, TariffPydantic


async def load_tariffs(tariffs):
    """Replaces tariffs with the new ones"""
    await Tariff.all().delete()
    cnt = 1
    for date in tariffs:
        for tariff_by_date in tariffs[date]:
            tariff_by_date["id"] = cnt
            tariff_by_date["date"] = date
            await Tariff.create(**tariff_by_date)
            cnt += 1


async def get_json_tariffs():
    """Returns a current tariffs in json format"""
    json_tariffs = {}
    for tariff in await TariffPydantic.from_queryset(Tariff.all()):
        json_tariffs[tariff.date] = \
            await Tariff.filter(date=tariff.date).values("cargo_type", "rate")
    return json_tariffs
