from models.tasks import CreateTask, UpdateTask, Task
from fastapi import APIRouter, Depends, Query, status
from services.task_repository import TaskRepository, get_task_repository

router = APIRouter(prefix="/tasks", tags=["Работа с задачами"])


@router.get("/", summary="Получить все задачи")
async def get_all_tasks(
    repo: TaskRepository = Depends(get_task_repository),
) -> list[Task]:
    return repo.get_all()


# Сортировка конечно дорогая, но пока так. Позже переедем на sqlite и будет order by
@router.get("/filtered", summary="Фильтрация и сортировка задач")
async def get_filtered_tasks(
    completed: bool | None = Query(
        default=None, description="Фильтр по статусу выполнения"
    ),
    sort_by: str | None = Query(default=None, description="Сортировка по id/title"),
    repo: TaskRepository = Depends(get_task_repository),
) -> list[Task]:
    
    response = repo.get_filtred(completed, sort_by)
    return response


@router.post("/", summary="Создать новую задачу", status_code=status.HTTP_201_CREATED)
async def create_tasks(
    new_task: CreateTask, repo: TaskRepository = Depends(get_task_repository)
) -> Task:
    response = repo.create(new_task)
    return response


@router.get("/{id}", summary="Получить задачу по id")
async def get_tasks_by_id(
    id: int, repo: TaskRepository = Depends(get_task_repository)
) -> Task:
    response = repo.get_by_id(id)
    return response


@router.delete(
    "/{id}", summary="Удалить задачу по id", status_code=status.HTTP_204_NO_CONTENT
)
async def delete_tasks(
    id: int, repo: TaskRepository = Depends(get_task_repository)
) -> None:
    _ = repo.delete_by_id(id)


@router.put("/{id}", summary="Обновить задачу по id")
async def update_tasks(
    id: int, new_data: UpdateTask, repo: TaskRepository = Depends(get_task_repository)
) -> Task:
    response = repo.update_by_id(id, new_data)
    return response
