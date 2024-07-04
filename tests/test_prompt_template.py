"""Test prompt_template.py"""
from prompt_template import getPromptTemplate

def test_get_prompt_template():
    """Test getting the prompt template."""
    template = getPromptTemplate()
    assert template is not None
    assert isinstance(template, str)
