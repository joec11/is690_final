# Standard library imports
from builtins import Exception, range, str
from datetime import datetime, timedelta
from unittest.mock import AsyncMock, patch
# from uuid import uuid4
import uuid

# Third-party imports
import pytest
from fastapi.testclient import TestClient
from httpx import AsyncClient
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker, scoped_session
from faker import Faker

# Application-specific imports
from app.main import app
from app.database import Base, Database
from app.models.api_model import UserQuery
from app.dependencies import get_db, get_settings
from app.utils.template_manager import TemplateManager
from app.services.email_service import EmailService

fake = Faker()

settings = get_settings()
TEST_DATABASE_URL = settings.database_url.replace("postgresql://", "postgresql+asyncpg://")
engine = create_async_engine(TEST_DATABASE_URL, echo=settings.debug)
AsyncTestingSessionLocal = sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)
AsyncSessionScoped = scoped_session(AsyncTestingSessionLocal)


# @pytest.fixture
# def email_service():
#     # Assuming the TemplateManager does not need any arguments for initialization
#     template_manager = TemplateManager()
#     email_service = EmailService(template_manager=template_manager)
#     return email_service


# This fixture creates the http client for your API tests
@pytest.fixture(scope="function")
async def async_client(db_session):
    async with AsyncClient(app=app, base_url="http://testserver") as client:
        app.dependency_overrides[get_db] = lambda: db_session
        try:
            yield client
        finally:
            app.dependency_overrides.clear()

@pytest.fixture(scope="session", autouse=True)
def initialize_database():
    try:
        Database.initialize(settings.database_url)
    except Exception as e:
        pytest.fail(f"Failed to initialize the database: {str(e)}")

# This function sets up and tears down (drops tables) for each test function, ensuring a clean database for each test.
@pytest.fixture(scope="function", autouse=True)
async def setup_database():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    yield
    async with engine.begin() as conn:
        # You can comment out this line during development if you are debugging a single test
        await conn.run_sync(Base.metadata.drop_all)
    await engine.dispose()

@pytest.fixture(scope="function")
async def db_session(setup_database):
    async with AsyncSessionScoped() as session:
        try:
            yield session
        finally:
            await session.close()

@pytest.fixture(scope="function")
async def UserQuery(db_session):
    userquery_data = {
        "id": uuid.uuid4(),
        "u_query": "This is a sample user query.",
        "query_timestamp": datetime.now(),
        "response_generated": True
    }
    userquery = UserQuery(**userquery_data)
    db_session.add(userquery)
    await db_session.commit()
    return userquery

# @pytest.fixture
# def email_service():
#     if settings.send_real_mail == 'true':
#         # Return the real email service when specifically testing email functionality
#         return EmailService()
#     else:
#         # Otherwise, use a mock to prevent actual email sending
#         mock_service = AsyncMock(spec=EmailService)
#         mock_service.send_verification_email.return_value = None
#         mock_service.send_user_email.return_value = None
#         return mock_service
