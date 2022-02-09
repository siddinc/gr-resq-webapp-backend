from pydantic import BaseModel, Field
from typing import UUID, Optional, EmailStr


class Author(BaseModel):
  ID: UUID = Field(...)
  firstName: Optional[str] = Field(None)
  lastName: Optional[str] = Field(None)
  institution: Optional[str] = Field(None)
  nanohubUserID: UUID = Field(...)
  userID: UUID = Field(...)
  submittedExperiments: Optional[list[UUID]] = Field([])
  authoredExperiments: Optional[list[UUID]] = Field([])