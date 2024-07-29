from fastapi import APIRouter, HTTPException
from fastapi.responses import JSONResponse
from pydantic import BaseModel
import logging

# Local imports
from app.dependencies import get_settings
from app.shared import chroma_db

# External dependencies from langchain
from langchain_openai import ChatOpenAI
from langchain.prompts import ChatPromptTemplate

# Initialize the API router and settings
router = APIRouter()
settings = get_settings()

class QueryText(BaseModel):
    query_text: str

@router.post("/generate/")
async def rag(query: QueryText):
    """
    Generate a response based on the provided query text using similarity search
    and a language model. The response includes the generated answer and source information.

    Args:
        query_text (str): The text of the query for which a response is to be generated.

    Returns:
        tuple: A tuple containing:
            - Original query text
            - An empty string (reserved for potential future use)
            - The prompt used for generating the response
            - An empty string (reserved for potential future use)
            - The formatted response with sources
    """
    try:
        text = query.query_text
        # Log the incoming query text
        logging.info(f"Received query: {text}")

        # Perform similarity search to find relevant documents
        results = chroma_db.similarity_search_with_relevance_scores(text)
        logging.debug(f"Similarity search results: {results}")

        # Check if any results were found and if the top result has sufficient relevance
        if not results or results[0][1] < settings.SIMILARITY_THRESHOLD:
            logging.error("No matching results found or relevance is below threshold.")
            return "Unable to find matching results."

        # Compile context text from the search results
        context_text = "\n\n---\n\n".join([doc.page_content for doc, _ in results])
        logging.info(f"Compiled context text: {context_text}")

        # Create and format the prompt template
        prompt_template = ChatPromptTemplate.from_template(settings.PROMPT_TEMPLATE)
        prompt = prompt_template.format(context=context_text, question=text)
        logging.debug(f"Formatted prompt: {prompt}")

        # Generate the response using the language model
        model = ChatOpenAI()
        response_text = model.predict(prompt)
        logging.info(f"Generated response: {response_text}")

        # Extract source information from the search results
        sources = [doc.metadata.get("source", "Unknown") for doc, _ in results]
        logging.debug(f"Sources: {sources}")

        # Format the final response
        formatted_response = f"{response_text}\n\nSources: {sources}"
        logging.info(f"Formatted response: {formatted_response}")

        response = {
            "query": text,
            "prompt": prompt,
            "formatted_response": formatted_response
        }
        
        return JSONResponse(content=response, status_code=200)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
