import json
from pathlib import Path
from exceptions.exceptions import Incorrect_data_exception, Tasks_not_found_exception
from models.tasks import CreateTask, Task, UpdateTask


class TaskRepository:
    def __init__(self, dir: str = "data", file: str = "tasks.json"):
        self.data_dir = Path(dir)
        self.data_file = self.data_dir / file
        self.tasks: list[Task] = self._load_tasks_from_file()

    def _load_tasks_from_file(self) -> list[Task]:
        if self.data_file.exists():
            with open(self.data_file, "r", encoding="utf-8") as f:
                data = json.load(f)
                return [Task(**item) for item in data]
        return []  # если файла нет

    def _save_tasks_to_file(self) -> None:
        self.data_dir.mkdir(exist_ok=True)
        with open(self.data_file, "w", encoding="utf-8") as f:
            json.dump(
                [task.model_dump() for task in self.tasks],
                f,
                indent=4,
                ensure_ascii=False,
            )

    def _generate_id(self) -> int:
        id = max((task.id for task in self.tasks), default=-1) + 1
        return id

    def get_all(self, is_completed: bool = None) -> list[Task]:
        if is_completed is None:
            return self.tasks
        result = [task for task in self.tasks if task.completed == is_completed]
        return result

    def get_by_id(self, id: int) -> Task:
        if id < 0:
            raise Incorrect_data_exception()
        required = list(filter(lambda task: task.id == id, self.tasks))
        if required:
            return required[0]
        raise Tasks_not_found_exception()

    def get_filtred(
        self, completed: bool | None = None, sort_by: str | None = None
    ) -> list[Task]:
        required = self.get_all(completed)
        if sort_by in ["id", "title"]:
            required.sort(key=lambda task: getattr(task, sort_by))
        return required

    def create(self, task: CreateTask) -> Task:
        id = self._generate_id()
        new_task = Task(id=id, **task.model_dump())
        self.tasks.append(new_task)
        self._save_tasks_to_file()
        return new_task

    def delete_by_id(self, id: int) -> None:
        for i, item in enumerate(self.tasks):
            if item.id == id:
                self.tasks.pop(i)
                self._save_tasks_to_file()
                return
        raise Tasks_not_found_exception()

    def update_by_id(self, id: int, new_data: UpdateTask) -> Task | None:
        for i, task in enumerate(self.tasks):
            if task.id == id:
                current_data = task.model_dump()
                updated_data = new_data.model_dump(exclude_unset=True)
                merge = {**current_data, **updated_data, "id": id}
                updated_task = Task(**merge)
                self.tasks[i] = updated_task
                self._save_tasks_to_file()
                return updated_task
        raise Tasks_not_found_exception()


def get_task_repository() -> TaskRepository:
    return TaskRepository()
