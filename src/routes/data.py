from fastapi import APIRouter, UploadFile
from helpers.config import settings
from controllers import DataController

data_router = APIRouter(
    prefix="/api/v1/data",
    tags=["api_v1"]
)

@data_router.post("/upload/{project_id}")
async def upload_data(project_id:str, file: UploadFile):

    is_valid = DataController.validate_uploading_file(file=file)

    return is_valid