from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel
from typing import List, Optional

app = FastAPI(title="Tasks API", description="RESTful API for task management")

# Pydantic model for input validation and data serialization
class Task(BaseModel):
    id: int
    title: str
    description: Optional[str] = None
    is_completed: bool = False

# In-memory database (to be replaced with PostgreSQL/SQLAlchemy in production)
tasks_db: List[Task] = []

@app.post("/tasks/", response_model=Task, status_code=status.HTTP_201_CREATED)
async def create_task(task: Task):
    """Create a new task and add it to the database."""
    if any(t.id == task.id for t in tasks_db):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Task with this ID already exists"
        )
    tasks_db.append(task)
    return task

@app.get("/tasks/", response_model=List[Task])
async def get_all_tasks():
    """Retrieve all tasks from the database."""
    return tasks_db

@app.get("/tasks/{task_id}", response_model=Task)
async def get_task_by_id(task_id: int):
    """Retrieve a specific task by its unique ID."""
    for task in tasks_db:
        if task.id == task_id:
            return task
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Task not found"
    )

@app.delete("/tasks/{task_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_task(task_id: int):
    """Delete a task by its ID."""
    global tasks_db
    tasks_db = [t for t in tasks_db if t.id != task_id]