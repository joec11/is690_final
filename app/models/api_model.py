from builtins import ValueError, bool, int, str
from datetime import datetime, timezone
from enum import Enum
import uuid
from sqlalchemy import (
    Column, ForeignKey, String, Integer, DateTime, Boolean, func, Enum as SQLAlchemyEnum
)
from sqlalchemy.dialects.postgresql import UUID, ENUM
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.database import Base
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.ext.asyncio import AsyncAttrs

class UserQuery(Base, AsyncAttrs):
    """
    Represents a user query within the application, corresponding to the 'user_queries' table in the database.
    This class uses SQLAlchemy ORM for mapping attributes to database columns efficiently.
    
    Attributes:
        id (UUID): Unique identifier for the user query.
        u_query (str): The query entered by the user.
        query_timestamp (datetime): Query Timestamp.
        response_generated (bool): Boolean flag to determine if a response was generated for the user query.
    """
    __tablename__ = "user_queries"
    __mapper_args__ = {"eager_defaults": True}

    id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    u_query: Mapped[str] = Column(String(2000), nullable=False)
    query_timestamp: Mapped[datetime] = Column(DateTime(timezone=True), server_default=func.now())
    response_generated: Mapped[bool] = Column(Boolean, default=False, nullable=False)
