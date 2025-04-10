import json
from pathlib import Path
from typing import List
from models.tasks import Task

DATA_DIR = Path("data")
DATA_FILE = DATA_DIR / "tasks.json"


def save_tasks_to_file(tasks: List[Task]) -> None:
    DATA_DIR.mkdir(exist_ok=True)
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(
            [task.model_dump() for task in tasks], f, indent=4, ensure_ascii=False
        )


def load_tasks_from_file() -> List[Task]:
    if DATA_FILE.exists():
        with open(DATA_FILE, "r", encoding="utf-8") as f:
            data = json.load(f)
            return [Task(**item) for item in data]
    return []  # если файла нет
