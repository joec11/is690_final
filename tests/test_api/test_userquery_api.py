from builtins import str
import pytest
from httpx import AsyncClient
from app.main import app
from app.models.api_model import UserQuery # Import your FastAPI app

# Example of a test function using the async_client fixture
@pytest.mark.asyncio
# async def test_create_userquery(async_client, mail_service):
async def test_create_userquery(async_client):
    # Define user query data for the test
    user_query_data = {
        "u_query": "This is a sample user query.",
    }
    # Send a POST request to create a user
    response = await async_client.post("/generate/", json=user_query_data)
    # Asserts
    assert response.status_code == 200
