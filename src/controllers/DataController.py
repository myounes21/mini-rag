from helpers.config import settings
from fastapi import UploadFile
from models import ResponseSignal


class DataController:

    @staticmethod
    def validate_uploading_file(file: UploadFile) -> tuple[bool, str]:
        if file.content_type not in settings.ALLOWED_FILE_TYPES:
            return False, ResponseSignal.FILE_TYPE_NOT_SUPPORTED.value

        if file.size > settings.MAX_FILE_SIZE_MB * 1024 * 1024: # 10m converted to bytes
                return False, ResponseSignal.FILE_SIZE_EXCEEDED.value

        return True, ResponseSignal.FILE_VALIDATED_SUCCESS.value