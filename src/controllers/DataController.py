from helpers.config import settings
from fastapi import UploadFile

class DataController:

    @staticmethod
    def validate_uploading_file(file: UploadFile) -> bool:
        if file.content_type not in settings.ALLOWED_FILE_TYPES:
            return False

        if file.size > settings.MAX_FILE_SIZE_MB * 1024 * 1024:
                return False

        return True