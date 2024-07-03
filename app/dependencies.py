from builtins import Exception, dict, list, str
import uuid
from fastapi import Depends, HTTPException, Header, Cookie, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.ext.asyncio import AsyncSession
from app.database import Database
from app.utils.template_manager import TemplateManager
# from app.services.email_service import EmailService
from settings.config import Settings
from sqlalchemy.exc import SQLAlchemyError

def get_settings() -> Settings:
    """Return application settings."""
    return Settings()

# def get_email_service() -> EmailService:
#     template_manager = TemplateManager()
#     return EmailService(template_manager=template_manager)

async def get_db() -> AsyncSession:
    """Dependency that provides a database session for each request."""
    async_session_factory = Database.get_session_factory()
    async with async_session_factory() as session:
        try:
            yield session
        except SQLAlchemyError as e:
            raise HTTPException(status_code=500, detail="Database error: " + str(e))
