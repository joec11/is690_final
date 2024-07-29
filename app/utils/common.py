import logging.config
import os
from app.dependencies import get_settings

# Retrieve settings from the application
settings = get_settings()

def setup_logging() -> logging.Logger:
    """
    Set up logging for the application using a configuration file.

    This function configures the logging settings based on a configuration file
    located in the project's root directory. It ensures consistent logging
    behavior across the application.

    Returns:
        logging.Logger: The configured logger instance.
    """
    # Determine the path to the 'logging.conf' file
    # Assumes the configuration file is located two directories up from the current file's directory (project root).
    logging_config_path = os.path.join(os.path.dirname(__file__), '..', '..', settings.LOGGING_CONFIGURATION)
    
    # Normalize the file path to resolve any '..' or other path components to an absolute path
    normalized_path = os.path.normpath(logging_config_path)
    
    # Apply the logging configuration from the file
    logging.config.fileConfig(normalized_path, disable_existing_loggers=False)
    
    # Return the logging module to allow further logging operations
    return logging.getLogger()
