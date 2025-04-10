from typing import List
from models.tasks import CreateTask, Task, UpdateTask
from utility.task_repository import load_tasks_from_file, save_tasks_to_file

tasks: List[Task] = load_tasks_from_file()


def get_tasks(is_completed: bool | None) -> List[Task]:
    if is_completed is None:
        return tasks

    result = [task for task in tasks if task.completed == is_completed]
    return result


def get_task_by_id(id: int) -> Task | None:
    for task in tasks:
        if task.id == id:
            return task

    return None


def create_new_tasks(task: CreateTask) -> Task:
    id = get_new_id()
    new_task = Task(id=id, **task.model_dump())
    tasks.append(new_task)
    save_tasks_to_file()
    return new_task


def delete_task_by_id(id: int) -> Task | None:
    for i, task in enumerate(tasks):
        if task.id == id:
            temp = tasks.pop(i)
            save_tasks_to_file()
            return temp
    return None


def update_task_by_id(id: int, new_data: UpdateTask) -> Task | None:
    for i, task in enumerate(tasks):
        if task.id == id:
            current_data = task.model_dump()
            updated_data = new_data.model_dump(exclude_unset=True)

            merge = {**current_data, **updated_data, "id": id}

            updated_task = Task(**merge)
            tasks[i] = updated_task
            save_tasks_to_file()
            return updated_task

    return None


def get_new_id() -> int:
    id = max((task.id for task in tasks), default=-1) + 1
    return id
