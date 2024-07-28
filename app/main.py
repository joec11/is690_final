# FastAPI imports
from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

# Local imports
from app.shared import logging, chroma_db
from app.routers import rag_routes

# Create an instance of FastAPI with configuration parameters
app = FastAPI(
    root_path="/api",
    title="FastAPI with RAG",
    version="0.0.1",
    contact={
        "name": "API Support",
        "url": "https://github.com/joec11/is690_final",
    },
    license_info={
        "name": "MIT",
        "url": "https://opensource.org/licenses/MIT"
    },
)

# Configure CORS middleware to allow requests from specified origins
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3001"],  # Update this to match your frontend app's URL
    allow_credentials=True,
    allow_methods=["*"],  # Allow all HTTP methods
    allow_headers=["*"],  # Allow all headers
)

# Event handler for application startup
@app.on_event("startup")
async def startup_event():
    """
    Event handler for application startup.

    Logs the startup event and initializes the Chroma database.
    """
    logging.info("FastAPI application starting up.")
    try:
        chroma_db.initialize()
        logging.info("Chroma database initialized successfully.")
    except Exception as e:
        logging.error(f"Failed to initialize Chroma database: {e}")

# Event handler for application shutdown
@app.on_event("shutdown")
async def shutdown_event():
    """
    Event handler for application shutdown.

    Cleans up the Chroma database and logs the shutdown event.
    """
    try:
        chroma_db.delete()
        logging.info("Chroma database deleted successfully.")
    except Exception as e:
        logging.error(f"Failed to delete Chroma database: {e}")
    logging.info("FastAPI application shutting down.")

# Include routers from the rag_routes module
app.include_router(rag_routes.router)
