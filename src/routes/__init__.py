from fastapi import APIRouter
from routes import base, data

api_router = APIRouter()

api_router.include_router(base.base_router)
api_router.include_router(data.data_router)