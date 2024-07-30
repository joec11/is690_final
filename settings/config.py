# Standard library imports
import os

# Third-party imports
from dotenv import find_dotenv, load_dotenv

# Local imports
from app.utils.prompt_template import getPromptTemplate

class Settings:
    """
    Settings class to manage configuration and environment variables for the application.
    """

    # Load environment variables from a .env file if it exists
    load_dotenv(find_dotenv())

    # OpenAI API key from environment variables, with a default fallback value
    OPENAI_API_KEY = os.getenv('OPENAI_API_KEY', 'default_openai_api_key')

    # Path to the Chroma directory, defaulting to 'chroma'
    CHROMA_PATH = os.getenv('CHROMA_DIR', 'chroma')

    # Path to the data directory, defaulting to 'data'
    DATA_PATH = os.getenv('DATA_DIR', 'data')

    # Chunk size for processing text, defaulting to 2700
    CHUNK_SIZE = int(os.getenv('CHUNK_SIZE', '2700'))

    # Overlap between text chunks, defaulting to 900
    CHUNK_OVERLAP = int(os.getenv('CHUNK_OVERLAP', '900'))

    # Similarity threshold for comparisons, defaulting to 0.7
    SIMILARITY_THRESHOLD = float(os.getenv('SIMILARITY_THRESHOLD', '0.7'))

    # Number of top K results to return in similarity searches, defaulting to 3
    SIMILARITY_SEARCH_TOP_K = int(os.getenv('SIMILARITY_SEARCH_TOP_K', '3'))

    # Path to the logging configuration file, defaulting to 'logging.conf'
    LOGGING_CONFIGURATION = os.getenv('LOG_CONFIG', 'logging.conf')

    # Path to the templates directory, defaulting to 'templates'
    TEMPLATES_PATH = os.getenv('TEMPLATES_DIR', 'templates')

    # Load the prompt template using a utility function
    PROMPT_TEMPLATE = getPromptTemplate()

    class Config:
        """
        Configuration settings for handling the environment file.
        """
        # Path to the .env file
        env_file = ".env"

        # Encoding used for the .env file
        env_file_encoding = 'utf-8'

# Instantiate the settings object to be used across the application
settings = Settings()
