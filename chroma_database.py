# Standard library imports
import os
import shutil

# Third-party imports
from dotenv import find_dotenv, load_dotenv
import openai

# Local imports
from langchain_community.document_loaders import DirectoryLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import Chroma
from configure_logging import createLogger

# Load environment variables
load_dotenv(find_dotenv())

# Set OpenAI API key with a default value if not provided
openai.api_key = os.getenv('OPENAI_API_KEY', 'default_openai_api_key')

# Constants with default values if not provided in environment variables
CHROMA_PATH = os.getenv('CHROMA_DIR', 'chroma')
DATA_PATH = os.getenv('DATA_DIR', 'data')

logging = createLogger(os.path.basename(__file__))

def create():
    delete()
    documents = load_documents()
    chunks = split_text(documents)
    save_to_chroma(chunks)
    logging.info("Chroma: create()")

def load_documents():
    loader = DirectoryLoader(DATA_PATH, glob=["*.csv", "*.txt"])
    logging.info("Chroma: load_documents()")
    return loader.load()

def split_text(documents):
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=600,
        chunk_overlap=200,
        length_function=len,
        add_start_index=True,
    )
    chunks = text_splitter.split_documents(documents)
    print(f"Split {len(documents)} documents into {len(chunks)} chunks.")
    logging.info("Chroma: split_text()")
    logging.info(f"Split {len(documents)} documents into {len(chunks)} chunks.")
    return chunks

def save_to_chroma(chunks):
    # Clear out the database first.
    if os.path.exists(CHROMA_PATH): \
        shutil.rmtree(CHROMA_PATH); \
        logging.info("Chroma: save_to_chroma() - Cleared the database")

    # Create a new DB from the documents.
    db = Chroma.from_documents(chunks, OpenAIEmbeddings(), persist_directory=CHROMA_PATH)
    db.persist()
    print(f"Saved {len(chunks)} chunks to {CHROMA_PATH}.")
    logging.info("Chroma: save_to_chroma() - Saved chunks to the chroma directory")

def delete():
    if os.path.exists(CHROMA_PATH):
        shutil.rmtree(CHROMA_PATH)
        print(f"Deleted Chroma directory at {CHROMA_PATH}.")
        logging.info("Chroma: delete() is true")
    else:
        print(f"Chroma directory at {CHROMA_PATH} does not exist.")
        logging.info("Chroma: delete() is false")
