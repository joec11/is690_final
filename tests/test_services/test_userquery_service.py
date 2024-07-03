import uuid
from datetime import datetime
from builtins import range
import pytest
from sqlalchemy import select
from app.dependencies import get_settings
from app.models.api_model import UserQuery
from app.exceptions.user_exceptions import NoResponseException
from app.services.api_service import UserQueryService

pytestmark = pytest.mark.asyncio

# Test creating a user with valid data
# async def test_create_userquery_with_valid_data(db_session, email_service):
async def test_create_userquery_with_valid_data(db_session):
    userquery_data = {
        "u_query": "This is a sample user query."
    }
    # user = await UserService.create(db_session, userquery_data, email_service)
    userquery = await UserQueryService.create_query(db_session, userquery_data)
    assert userquery is not None
    assert userquery.u_query == userquery_data["u_query"]
