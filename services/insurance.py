from models import Tariff, Cargo, TariffPydantic


async def calculate_insurance_cost(cargo):
    tariff_qs = Tariff.filter(date=cargo.date, cargo_type=cargo.cargo_type).get()
    tariff = await TariffPydantic.from_queryset_single(tariff_qs)
    cargo.insurance_cost = cargo.declared_cost * tariff.rate
