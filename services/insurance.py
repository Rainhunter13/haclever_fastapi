"""Insurance related services"""

from models import Tariff, TariffPydantic


async def calculate_insurance_cost(cargo):
    """Returns a cargo object with calculated insurance cost"""
    tariff_qs = Tariff.filter(date=cargo.date, cargo_type=cargo.cargo_type).get()
    tariff = await TariffPydantic.from_queryset_single(tariff_qs)
    cargo.insurance_cost = cargo.declared_cost * tariff.rate
