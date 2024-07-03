import uuid
import pytest
from pydantic import ValidationError
from datetime import datetime
from app.schemas.api_schemas import UserQueryBase, UserQueryResponse

# Fixtures for common test data
@pytest.fixture
def userquery_base_data():
    return {
        "u_query": "A sample user query."
    }

@pytest.fixture
def userquery_response_data(userquery_base_data):
    return {
        "id": uuid.uuid4(),
        "query_timestamp": datetime.now(),
        "response_generated": True
    }
