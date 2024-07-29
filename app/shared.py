# Local imports
from app.chroma_database import Chroma_Database
from app.utils.common import setup_logging

# Initialize the Chroma database instance
chroma_db = Chroma_Database()

# Set up logging configuration
# This function configures the logging settings based on a configuration file.
logging = setup_logging()
