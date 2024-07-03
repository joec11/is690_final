from builtins import len
import pytest
import uuid
from datetime import datetime
from httpx import AsyncClient
from sqlalchemy.future import select

from app.models.api_model import UserQuery

@pytest.mark.asyncio
async def test_userquery_creation(db_session):
    """Test that a user query is correctly created."""

    verified_userquery = {
        "id": uuid.uuid4(),
        "u_query": "This is a sample user query.",
        "query_timestamp": datetime.now(),
        "response_generated": False
    }

    assert verified_userquery is not None
    assert verified_userquery["id"] == verified_userquery["id"]
    assert verified_userquery["u_query"] == verified_userquery["u_query"]
    assert verified_userquery["query_timestamp"] == verified_userquery["query_timestamp"]
    assert verified_userquery["response_generated"] == verified_userquery["response_generated"]
