import logging
import logging.config
import os

def createLogger(file_name: str):
    """Configure Logging to allow logging application activity"""
    logging_conf_path = 'logging.conf'
    if os.path.exists(logging_conf_path):
        logging.config.fileConfig(logging_conf_path, disable_existing_loggers=False)
    else:
        logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
    
    logger = logging.getLogger(__name__)
    logger.info("Logging configured for " + file_name)
    
    return logger
