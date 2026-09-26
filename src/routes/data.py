import os.path
from helpers.config import settings
from fastapi import APIRouter, UploadFile, status
from fastapi.responses import JSONResponse
from controllers import DataController, ProjectController
import aiofiles

data_router = APIRouter(
    prefix="/api/v1/data",
    tags=["api_v1"]
)

@data_router.post("/upload/{project_id}")
async def upload_data(project_id:str, file: UploadFile):

    # no need for making instance because the function is static
    is_valid, signal = DataController.validate_uploading_file(file=file)

    if not is_valid:
        return JSONResponse(
            status_code=status.HTTP_400_BAD_REQUEST,
            content={
                "signal":signal
            }
        )

    project_dir_path = ProjectController().get_project_path(project_id=project_id)
    file_path = project_dir_path / file.filename

    async with aiofiles.open(file_path, "wb") as f:
        while chunk := await file.read(settings.FILE_DEFAULT_CHUNK_SIZE):
            await f.write(chunk)

    return JSONResponse(
        content={
            "signal":signal
        }
    )