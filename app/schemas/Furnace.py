from pydantic import BaseModel, Field
from typing import UUID, Optional

class Furnace(BaseModel):
  ID: UUID = Field(...)
  experiments: Optional[list[UUID]] = Field([])
  tubeDiameter: Optional[float] = Field(None)
  tubeLength: Optional[float] = Field(None)
  crossSectionalArea: Optional[float] = Field(None)
  lengthOfHeatedRegion: Optional[float] = Field(None)