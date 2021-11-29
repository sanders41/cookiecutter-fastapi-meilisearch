from app.api.api_v1.api import api_router
from app.core.config import settings
from fastapi import FastAPI

app = FastAPI()
app.include_router(api_router, prefix=settings.API_V1_STR)
