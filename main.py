from fastapi import FastAPI
from tortoise.contrib.fastapi import register_tortoise
from urllib.parse import quote_plus
from typing import List, Dict

from models import Cargo, Tariff, TariffPydantic, CargoPydantic
from services.insurance import calculate_insurance_cost
from services.tariffs import load_tariffs, get_json_tariffs

db_password = quote_plus("Rainhunter13?")

app = FastAPI()

register_tortoise(
    app,
    db_url="postgres://rainhunter_db:" + db_password + "@localhost:5432/haclever_db",
    modules={"models": ["models"]},
    generate_schemas=True,
    add_exception_handlers=True,
)


@app.get("/tariffs")
async def get_tariffs():
    return await get_json_tariffs()


@app.post("/tariffs")
async def post_tariffs(tariffs: Dict):
    await load_tariffs(tariffs)
    return await get_json_tariffs()


@app.post("/insurance_cost", response_model=CargoPydantic)
async def insurance_cost(cargo: CargoPydantic):
    await calculate_insurance_cost(cargo)
    await Cargo.create(**cargo.dict())
    return cargo


@app.get("/cargos", response_model=List[CargoPydantic])
async def get_cargos():
    return await CargoPydantic.from_queryset(Cargo.all())
