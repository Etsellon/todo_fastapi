from typing import Annotated
from pydantic import BaseModel, Field


class Task(BaseModel):
    id: Annotated[int, Field(default=1, ge=1, description="Идентификатор задачи")]
    title: Annotated[str, Field(default="Новая задача", title="Название задачи")]
    description: Annotated[str | None, Field(default="", title="Описание задачи")]
    completed: Annotated[bool, Field(default=False)]


class CreateTask(BaseModel):
    title: Annotated[str, Field(default="Новая задача", title="Название задачи")]
    description: Annotated[str | None, Field(default="", title="Описание задачи")]
    completed: Annotated[bool, Field(default=False)]


class UpdateTask(BaseModel):
    title: Annotated[str | None, Field(default=None, title="Название задачи")]
    description: Annotated[str | None, Field(default=None, title="Описание задачи")]
    completed: Annotated[bool | None, Field(default=None)]
