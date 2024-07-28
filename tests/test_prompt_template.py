"""Test prompt_template.py"""
from app.utils.prompt_template import getPromptTemplate

def test_get_prompt_template():
    """Test the retrieval of the prompt template."""

    # Retrieve the prompt template using the function
    template = getPromptTemplate()

    # Check that the template is not None
    assert template is not None, "Prompt template should not be None"

    # Check that the template is of type string
    assert isinstance(template, str), "Prompt template should be a string"
