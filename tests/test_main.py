# pylint: disable=too-few-public-methods, unnecessary-pass, redefined-outer-name
"""Test main.py"""
import os
from unittest.mock import patch
import pytest
from fastapi.testclient import TestClient
from main import app  # Assuming your FastAPI instance is named 'app'
import chroma_database

class MockChroma:
    """Mocking the database and dependencies"""
    def similarity_search_with_relevance_scores(self):
        """Simulating DB search results"""
        return [
            ({'page_content': 'Mock content 1', 'metadata': {'source': 'Source A'}}, 0.8),
            ({'page_content': 'Mock content 2', 'metadata': {'source': 'Source B'}}, 0.75),
            ({'page_content': 'Mock content 3', 'metadata': {'source': 'Source C'}}, 0.72)
        ]

class MockOpenAIEmbeddings:
    """Empty MockOpenAIEmbeddings Class"""
    pass

class MockChatOpenAI:
    """MockChatOpenAI Class with a predict method"""
    def predict(self):
        """Return a mock response from OpenAI."""
        return "Mock response from OpenAI"

@pytest.fixture(scope="module")
def test_client():
    """Setup"""
    os.environ['CHROMA_DIR'] = 'chroma'
    with patch('main.OpenAIEmbeddings', MockOpenAIEmbeddings):
        with patch('main.Chroma', MockChroma):
            client = TestClient(app)
            yield client
    # Teardown

def test_generate_endpoint(test_client):
    """Test case 1: Valid query with sufficient match"""
    query = "Give me a list of the top five cryptocurrencies."
    response = test_client.get(f"/generate/?query_text={query}")
    assert response.status_code == 200
    assert f"Query: {query}" in response.text
    assert "Response: " in response.text
    assert "Sources: " in response.text

    # Test case 2: Query with insufficient match
    query = "invalid query"
    with patch.object(MockChroma, 'similarity_search_with_relevance_scores', return_value=[]):
        response = test_client.get(f"/generate/?query_text={query}")
        assert response.status_code == 200
        assert "Unable to find matching results." in response.text

    chroma_database.delete()
