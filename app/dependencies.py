# Local imports
from settings.config import Settings

def get_settings() -> Settings:
    """
    Retrieve application settings.

    This function creates and returns an instance of the Settings class, 
    which contains the configuration and environment variables required for 
    the application.

    Returns:
        Settings: An instance of the Settings class containing application configuration.
    """
    # Create and return an instance of the Settings class
    return Settings()
