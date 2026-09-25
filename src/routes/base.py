from fastapi import APIRouter
from helpers.config import settings

base_router = APIRouter(
    prefix="/api/v1",
    tags=["api_v1"]
)

@base_router.get("/")
async def welcome():

    return {
        "name": settings.APP_NAME,
        "version":  settings.APP_VERSION

    }