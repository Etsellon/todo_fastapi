from typing import List
from services.task_services import (
    create_new_tasks,
    delete_task_by_id,
    get_task_by_id,
    get_tasks,
    update_task_by_id,
)
from models.tasks import CreateTask, UpdateTask, Task

from fastapi import APIRouter, HTTPException, Query


router = APIRouter(prefix="/tasks", tags=["Работа с задачами"])


@router.get("/", summary="Получить все задачи")
async def get_all_tasks() -> List[Task]:
    response = get_tasks()
    return response


@router.get("/filtered", summary="Фильтрация и сортировка задач")
async def get_filtered_tasks(
    completed: bool | None = Query(
        default=None, description="Фильтр по статусу выполнения (true/false)"
    ),
    sort_by: str | None = Query(default=None, description="Сортировка по id/title"),
) -> List[Task]:
    response = get_tasks(is_completed=completed)
    if sort_by in ["id", "title"]:
        response.sort(key=lambda task: getattr(task, sort_by))
    return response


@router.post("/", summary="Создать новую задачу")
async def create_tasks(new_task: CreateTask) -> Task:
    response = create_new_tasks(new_task)
    return response


@router.get("/{id}", summary="Получить задачу по id")
async def get_tasks_by_id(id: int) -> Task:
    if id < 0:
        raise HTTPException(400, "Некорректные данные")
    response = get_task_by_id(id)
    if response is None:
        raise HTTPException(404, "Задача не найдена")
    return response


@router.delete("/{id}", summary="Удалить задачу по id")
async def delete_tasks(id: int) -> Task:
    response = delete_task_by_id(id)
    if response is None:
        raise HTTPException(404, "Задача не найдена")
    return response


@router.put("/{id}", summary="Обновить задачу по id")
async def update_tasks(id: int, new_data: UpdateTask) -> Task:
    response = update_task_by_id(id, new_data)

    if response is None:
        raise HTTPException(404, "Задача не найдена")
    return response
