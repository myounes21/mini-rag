from pathlib import Path

class BaseController:
    BASE_DIR = Path(__file__).resolve().parents[1]
    FILES_DIR = BASE_DIR / "assets" / "files"