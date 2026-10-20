import json

from pydantic import BaseModel, TypeAdapter


class Cat(BaseModel):
    name: str
    color: str


class Dog(BaseModel):
    name: str
    breed: str


ta = TypeAdapter(Cat | Dog)
ta_schema = ta.json_schema()
print(json.dumps(ta_schema, indent=2))
