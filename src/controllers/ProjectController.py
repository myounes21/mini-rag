from .BaseController import BaseController
from pathlib import Path

class ProjectController(BaseController):

    def get_project_path(self, project_id: str) -> Path:

        project_dir = self.FILES_DIR / project_id
        project_dir.mkdir(parents=True, exist_ok=True)

        return project_dir