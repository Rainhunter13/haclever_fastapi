from tortoise.models import Model
from tortoise import fields


class Tariff(Model):
    date = fields.DateField(default=None)
    cargo_type = fields.CharField(max_length=100, default=None)
    rate = fields.FloatField(default=None)


class Cargo(Model):
    cargo_type = fields.CharField(max_length=100, default=None)
    declared_cost = fields.FloatField(default=None)
    insurance_cost = fields.FloatField(default=None)
