from fastapi import APIRouter
from helpers.config import settings

router = APIRouter(
    prefix="/api/v1",
    tags=["api_v1"]
)

@router.get("/")
async def welcome():

    app_name = settings.APP_NAME
    app_version = settings.APP_VERSION

    return {
        "name": app_name,
        "version": app_version
    }