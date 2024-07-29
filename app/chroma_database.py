import logging
import os
import shutil

# Third-party imports
import openai
from langchain_community.document_loaders import DirectoryLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import Chroma

class Chroma_Database:
    """
    Class for managing a Chroma database, including initialization, 
    creation, deletion, document loading, text splitting, and chunk saving.
    """

    # Class-level attribute for Chroma database instance
    chroma_db = None

    @classmethod
    def initialize(cls):
        """
        Initialize the Chroma database. This includes:
        - Deleting any existing database
        - Loading documents
        - Splitting text into chunks
        - Saving chunks to the database

        This method configures the OpenAI API key and sets up the Chroma database.
        """
        from app.dependencies import get_settings
        settings = get_settings()
        openai.api_key = settings.OPENAI_API_KEY

        cls.create()  # Create a new Chroma database
        embedding_function = OpenAIEmbeddings()
        Chroma(persist_directory=settings.CHROMA_PATH, embedding_function=embedding_function)
        logging.info("Chroma database initialized.")

    @classmethod
    def create(cls):
        """
        Create the Chroma database by:
        - Deleting existing database
        - Loading documents
        - Splitting text into chunks
        - Saving chunks to the database
        """
        try:
            cls.delete()  # Delete existing database if it exists
            documents = cls.load_documents()  # Load documents
            chunks = cls.split_text(documents)  # Split documents into chunks
            cls.save_to_chroma(chunks)  # Save chunks to the Chroma database
            logging.info("Chroma database created successfully.")
        except Exception as e:
            logging.error(f"Failed to create Chroma database: {e}")
            raise

    @classmethod
    def delete(cls):
        """
        Delete the Chroma database directory if it exists.
        """
        from app.dependencies import get_settings
        settings = get_settings()

        if os.path.exists(settings.CHROMA_PATH):
            shutil.rmtree(settings.CHROMA_PATH)
            logging.info("Chroma database directory deleted.")
        else:
            logging.info("Chroma database directory does not exist.")

    @classmethod
    def load_documents(cls):
        """
        Load documents from the specified directory. Only .csv and .txt files are considered.

        Returns:
            list: A list of loaded documents.
        """
        from app.dependencies import get_settings
        settings = get_settings()

        try:
            loader = DirectoryLoader(settings.DATA_PATH, glob=["*.csv", "*.txt"])
            documents = loader.load()
            logging.info(f"Loaded {len(documents)} documents.")
            return documents
        except Exception as e:
            logging.error(f"Failed to load documents: {e}")
            raise

    @classmethod
    def split_text(cls, documents):
        """
        Split the loaded documents into text chunks.

        Args:
            documents (list): List of documents to be split.

        Returns:
            list: List of text chunks.
        """
        from app.dependencies import get_settings
        settings = get_settings()

        text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=settings.CHUNK_SIZE,
            chunk_overlap=settings.CHUNK_OVERLAP,
            length_function=len,
            add_start_index=True,
        )
        chunks = text_splitter.split_documents(documents)
        logging.info(f"Split {len(documents)} document(s) into {len(chunks)} chunks.")
        return chunks
    
    @classmethod
    def save_to_chroma(cls, chunks):
        """
        Save text chunks to the Chroma database. Clears existing database directory before saving.

        Args:
            chunks (list): List of text chunks to be saved.
        """
        from app.dependencies import get_settings
        settings = get_settings()

        try:
            # Clear existing database directory
            if os.path.exists(settings.CHROMA_PATH):
                shutil.rmtree(settings.CHROMA_PATH)
                logging.info("Cleared the existing Chroma database directory.")
            
            # Save new chunks to the database
            cls.chroma_db = Chroma.from_documents(chunks, OpenAIEmbeddings(), persist_directory=settings.CHROMA_PATH)
            cls.chroma_db.persist()
            logging.info("Chunks saved to the Chroma database.")
        except Exception as e:
            logging.error(f"Failed to save chunks to Chroma: {e}")
            raise

    @classmethod
    def similarity_search_with_relevance_scores(cls, query_text):
        """
        Perform a similarity search with relevance scores using the Chroma instance.

        Args:
            query_text (str): The query text to search for.

        Returns:
            List[Tuple[Document, float]]: A list of tuples containing the matching documents and their relevance scores.
        """
        if not cls.chroma_db:
            raise ValueError("Chroma database has not been initialized.")
        
        from app.dependencies import get_settings
        settings = get_settings()

        results = cls.chroma_db.similarity_search_with_relevance_scores(query_text, k=settings.SIMILARITY_SEARCH_TOP_K)
        logging.info(f"Performed similarity search for query: '{query_text}'. Found {len(results)} results.")
        return results
