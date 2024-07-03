from builtins import Exception, bool, classmethod, int, len, str
from datetime import datetime, timezone
from typing import Optional, Dict, List
from pydantic import ValidationError
from sqlalchemy import update, select
from sqlalchemy.ext.asyncio import AsyncSession
from app.dependencies import get_settings
from app.models.api_model import UserQuery
from app.schemas.api_schemas import UserQueryBase
from app.services.db_service import DbService
from uuid import UUID
# from app.services.email_service import EmailService
from app.exceptions.user_exceptions import NoResponseException

settings = get_settings()

class UserQueryService(DbService):

    @classmethod
    # async def create(cls, session: AsyncSession, user_data: Dict[str, str], email_service: EmailService) -> User:
    async def create_query(cls, session: AsyncSession, user_data: Dict[str, str]) -> UserQuery:
        try:
            validated_data = UserQueryBase(**user_data).model_dump()
            new_user_query = UserQuery(**validated_data)
            session.add(new_user_query)
            await session.commit()
            # await email_service.send_verification_email(new_user)
            return new_user_query
        except ValidationError as e:
            raise e

    @classmethod
    async def count(cls, session: AsyncSession) -> int:
        query = select(UserQuery)
        result = await session.execute(query)
        return len(result.scalars().all())
