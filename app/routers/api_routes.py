from builtins import Exception, dict, int, len, print, str
from datetime import timedelta
import logging
from fastapi import APIRouter, Depends, HTTPException, Request, Response, Security, status, Body
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
import jwt
from sqlalchemy.ext.asyncio import AsyncSession
# from app.dependencies import get_db, get_email_service
from app.dependencies import get_db
from app.schemas.api_schemas import UserQueryBase, UserQueryResponse
from app.services.api_service import UserQueryService
from app.dependencies import get_settings
# from app.services.email_service import EmailService
from app.exceptions.user_exceptions import NoResponseException
from uuid import UUID
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm

router = APIRouter()
settings = get_settings()

@router.post("/generate/", response_model=UserQueryResponse, tags=["Enter Query"])
# async def register(user_data: UserCreate = Body(...), session: AsyncSession = Depends(get_db), email_service: EmailService = Depends(get_email_service)):
async def generate(user_query_data: UserQueryBase = Body(...), session: AsyncSession = Depends(get_db)):
    try:
        # user = await UserService.register_user(session, user_data.model_dump(), email_service)
        user_query = await UserQueryService.create_query(session, user_query_data.model_dump())
        return UserQueryResponse.model_construct(
            id=user_query.id,
            u_query=user_query.u_query,
            query_timestamp= user_query.query_timestamp,
            response_generated=user_query.response_generated
        )
    except NoResponseException as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))
