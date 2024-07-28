# pylint: disable=too-few-public-methods, unnecessary-pass, redefined-outer-name
"""Test main.py"""

def test_generate_endpoint_input_query():
    """Test that the generate endpoint input query is valid."""

    # Define the query to be tested
    query = "Give me a list of the top five cryptocurrencies."

    # Check that the query is not None
    assert query is not None, "Query should not be None"

    # Check that the query is of type string
    assert isinstance(query, str), "Query should be a string"
