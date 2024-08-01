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

# Define the model for query text input
class QueryText(BaseModel):
    query_text: str

# Route to handle query submissions and generate responses
@router.post("/generate")
async def rag(query: QueryText):
    """
    Generate a response based on the provided query text using similarity search
    and a language model. The response includes the generated answer and source information.

    Args:
        query (QueryText): The query text encapsulated in a Pydantic model.

    Returns:
        JSONResponse: A JSON response containing the query, prompt, and formatted response.
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
            return JSONResponse(content={"error": "Unable to find matching results."}, status_code=404)

        # Compile context text from the search results
        context_text = "\n\n---\n\n".join([doc.page_content for doc, _ in results])
        logging.info(f"Compiled context text: {context_text}")

        # Create and format the prompt template
        prompt_template = ChatPromptTemplate.from_template(settings.PROMPT_TEMPLATE)
        prompt = prompt_template.format(context=context_text, question=text)
        logging.debug(f"Formatted prompt: {prompt}")

        # Generate the response using the language model
        model = ChatOpenAI(openai_api_key=settings.OPENAI_API_KEY, model=settings.OPENAI_MODEL)
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
        # Handle and log unexpected errors
        logging.error(f"An error occurred: {e}")
        raise HTTPException(status_code=500, detail=str(e))
