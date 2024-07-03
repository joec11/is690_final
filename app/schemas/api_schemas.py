from builtins import ValueError, any, bool, str
from pydantic import BaseModel, EmailStr, Field, validator, root_validator
from typing import Optional, List
from datetime import datetime
from enum import Enum
import uuid
import re

class UserQueryBase(BaseModel):
    u_query: str = Field(..., example="A sample user query.")

    class Config:
        from_attributes = True

# class UserQueryCreate(UserQueryBase):
#     query_timestamp: datetime = Field(..., example=datetime.now())

class UserQueryResponse(UserQueryBase):
    id: uuid.UUID = Field(..., example=uuid.uuid4())
    query_timestamp: datetime = Field(..., example=datetime.now())
    response_generated: bool = Field(default=False, example=True)

class ErrorResponse(BaseModel):
    error: str = Field(..., example="Not Found")
    details: Optional[str] = Field(None, example="The requested resource was not found.")
