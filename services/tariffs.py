from models import Tariff


async def load_tariffs(tariffs):
    await Tariff.all().delete()
    cnt = 1
    for date in tariffs:
        for tariff_by_date in tariffs[date]:
            tariff_by_date["id"] = cnt
            tariff_by_date["date"] = date
            await Tariff.create(**tariff_by_date)
            cnt += 1
