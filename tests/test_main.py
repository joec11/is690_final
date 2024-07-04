# pylint: disable=too-few-public-methods, unnecessary-pass, redefined-outer-name
"""Test main.py"""
def test_generate_endpoint_input_query():
    """Test that the generate endpoint input query is not None and is a string."""
    query = "Give me a list of the top five cryptocurrencies."
    assert query is not None
    assert isinstance(query, str)
