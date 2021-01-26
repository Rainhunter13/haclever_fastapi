from fastapi import FastAPI
from tortoise.contrib.fastapi import register_tortoise
from urllib.parse import quote_plus
from typing import List

from models import Cargo, Tariff, TariffPydantic, CargoPydantic

db_password = quote_plus("Rainhunter13?")

app = FastAPI()

register_tortoise(
    app,
    db_url="postgres://rainhunter_db:" + db_password + "@localhost:5432/haclever_db",
    modules={"models": ["models"]},
    generate_schemas=True,
    add_exception_handlers=True,
)


@app.get("/tariff", response_model=List[TariffPydantic])
async def get_tariff():
    return await TariffPydantic.from_queryset(Tariff.all())


@app.post("/tariff")
async def post_tariff(tariff: TariffPydantic):
    await Tariff.create(**tariff.dict(exclude_unset=True))
    return tariff


@app.post("/insurance_cost")
def calculate_insurance_cost(cargo: CargoPydantic):
    return cargo
