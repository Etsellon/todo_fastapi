# FastAPI Task Manager
Простой API-сервис для управления задачами (todo), построенный на FastAPI.  
Данные сохраняются в JSON-файл `tasks.json`.

## Стек технологий
- [FastAPI](https://fastapi.tiangolo.com/) — высокопроизводительный веб-фреймворк
- [Pydantic](https://docs.pydantic.dev/) — валидация данных
- [Uvicorn](https://www.uvicorn.org/) — ASGI-сервер
- Python 3.12+

## Установка и запуск
```bash
git clone https://github.com/Etsellon/todo_fastapi.git
cd todo_fastapi
python -m venv .venv
.venv\Scripts\activate   # Windows
pip install -r requirements.txt
uvicorn main:app --reload
```

## Возможности
- Получение всех задач или по статусу
- Создание новой задачи
- Обновление задачи
- Удаление задачи
- Хранение задач в `data/tasks.json`