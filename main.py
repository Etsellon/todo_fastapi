from fastapi import FastAPI
import uvicorn

from api.v1.routers.task_router import router as task_router

app = FastAPI()


@app.get("/")
async def root() -> dict[str, str]:
    return {"message": "Hello world!"}


app.include_router(task_router)


if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8000)
