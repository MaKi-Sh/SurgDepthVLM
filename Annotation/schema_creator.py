import json 
from typing import Literal, Annotated
from pydantic import BaseModel, Field, ConfigDict
class Polygon(BaseModel): 
    model_config = ConfigDict(extra='forbid')
    vertices: list[tuple[Annotated[float, Field(ge=0)], Annotated[float, Field(ge=0)]]] = Field(min_length=3)

class Scissors(BaseModel):
    model_config = ConfigDict(extra='forbid')
    tooltype: Literal["monopolar_curved_scissors"]
    state: Literal["open", "closed", "unclear"]

class Forceps(BaseModel):
    model_config = ConfigDict(extra='forbid')
    tooltype: Literal["bipolar_forceps", "prograsp_forceps"]
    state: Literal["open", "closed", "holding", "unclear"]

class Suction(BaseModel):
    model_config = ConfigDict(extra='forbid')
    tooltype: Literal["suction"]
    state: Literal["on", "off", "unclear"]

class NeedleDriver(BaseModel):
    model_config = ConfigDict(extra='forbid')
    tooltype: Literal["large_needle_driver"]
    state: Literal["open", "closed", "holding", "unclear"]
    contact_with_needle: Literal["true", "false", "unclear"]| None = None

class Stapler(BaseModel):
    model_config = ConfigDict(extra='forbid')
    tooltype: Literal["stapler"]
    state: Literal["open", "closed", "firing", "unclear"] | None = None

class MiscAndOther(BaseModel): 
    model_config = ConfigDict(extra='forbid')
    tooltype: Literal["suturing_needle", "clamps", "ultrasound_probe", "other"]

class Tools(BaseModel):
    model_config = ConfigDict(extra='forbid')
    id: str
    tool: Scissors | Forceps | Suction | NeedleDriver | Stapler | MiscAndOther = Field(discriminator="tooltype") 
    depth_layer: int| Literal["unclear"]| None = None
    geometry: Polygon
    contact: Literal["true", "false", "unclear"] | None = None
    contact_loc: Polygon | None = None
    action_state: Literal["Idle", "Grasping", "Retraction", "Tissue Manipulation", "Tool Manipulation", "Cutting", "Cauterization", "Suction", "Looping", "Suturing", "Staple", "Ultrasound Sensing", "Clipping", "Other"] | None = None
class Tissue(BaseModel): 
    model_config = ConfigDict(extra='forbid')
    id: str
    tissue_type: str 
    geometry: Polygon

class Frame(BaseModel): 
    model_config = ConfigDict(extra='forbid')
    tissue: list[Tissue] | None = None 
    tools: list[Tools] | None = None 

main_model_schema = Frame.model_json_schema()
with open("schema.json", "w", encoding="utf-8") as f:
    json.dump(main_model_schema, f, indent=4)
