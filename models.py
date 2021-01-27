from tortoise.models import Model
from tortoise import fields
from tortoise.contrib.pydantic import pydantic_model_creator


class Tariff(Model):
    id = fields.IntField(pk=True)

    date = fields.DateField(default=None)
    cargo_type = fields.CharField(max_length=100, default=None)
    rate = fields.FloatField(default=None)


class Cargo(Model):
    id = fields.IntField(pk=True)

    date = fields.DateField(default=None)
    cargo_type = fields.CharField(max_length=100, default=None)
    declared_cost = fields.FloatField(default=None)
    insurance_cost = fields.FloatField(default=None, null=True)


TariffPydantic = pydantic_model_creator(Tariff, name="TariffPydantic")
CargoPydantic = pydantic_model_creator(Cargo, name="CargoPydantic")
