from fastapi import APIRouter
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from starlette.requests import Request

# Local imports
from app.dependencies import get_settings

# Initialize the API router and settings
router = APIRouter()
settings = get_settings()

# Initialize the Jinja2 templates
templates = Jinja2Templates(directory=settings.TEMPLATES_PATH)

# Route to render the RAG HTML template
@router.get("/", response_class=HTMLResponse)
async def rag(request: Request):
    """
    Renders the RAG HTML template.

    Args:
        request (Request): The HTTP request object.

    Returns:
        HTMLResponse: The rendered HTML template for RAG.
    """
    return templates.TemplateResponse("rag.html", {"request": request})
