"""REST API for working with cargo insurances"""

from urllib.parse import quote_plus
from typing import List, Dict
from fastapi import FastAPI
from tortoise.contrib.fastapi import register_tortoise

from models import Cargo, CargoPydantic
from services.insurance import calculate_insurance_cost
from services.tariffs import load_tariffs, get_json_tariffs

db_password = quote_plus("Rainhunter13?")

app = FastAPI()

register_tortoise(
    app,
    db_url="postgres://rainhunter_db:" + db_password + "@db:5432/haclever_db",
    modules={"models": ["models"]},
    generate_schemas=True,
    add_exception_handlers=True,
)


@app.get("/tariffs")
async def get_tariffs():
    """Returns a json representation of current tariffs"""
    return await get_json_tariffs()


@app.post("/tariffs")
async def post_tariffs(tariffs: Dict):
    """Replaces tariffs with new ones from a json file"""
    await load_tariffs(tariffs)
    return await get_json_tariffs()


@app.post("/insurance_cost", response_model=CargoPydantic)
async def insurance_cost(cargo: CargoPydantic):
    """Calculates insurance cost for a cargo object and returns the updated one"""
    await calculate_insurance_cost(cargo)
    await Cargo.create(**cargo.dict())
    return cargo


@app.get("/cargos", response_model=List[CargoPydantic])
async def get_cargos():
    """Returns the list of all cargos"""
    return await CargoPydantic.from_queryset(Cargo.all())
