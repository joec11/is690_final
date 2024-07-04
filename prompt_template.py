def getPromptTemplate():
    prompt_template = """
Answer the question based only on the following context:

{context}

---

Answer the question based on the above context: {question}
"""
    return prompt_template
