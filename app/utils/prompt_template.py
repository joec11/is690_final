def getPromptTemplate() -> str:
    """
    Generate and return a prompt template for question answering.

    This function constructs a prompt template that includes:
    - A section for providing context
    - A section for posing the question

    Returns:
        str: A string containing the prompt template with placeholders for context and question.
    """
    # Define the prompt template with placeholders for context and question
    prompt_template = """
    Answer the question based only on the following context:

    {context}

    ---

    Answer the question based on the above context: {question}
    """
    
    # Return the prompt template as a string
    return prompt_template
