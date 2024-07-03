from builtins import repr
from datetime import datetime, timedelta, timezone
import pytest
import uuid
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from app.models.api_model import UserQuery
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.database import Base

@pytest.mark.asyncio
async def test_userquery(db_session: AsyncSession):
    # Create a user query object without specifying optional fields
    user_query = UserQuery(u_query="Another test query")

    user_query.id = uuid.uuid4()
    user_query.query_timestamp = datetime.now()
    user_query.response_generated = True

    # Assert that the values are correctly applied
    assert user_query.id is not None
    assert user_query.u_query == "Another test query"
    assert isinstance(user_query.query_timestamp, datetime)
    assert user_query.response_generated == True
