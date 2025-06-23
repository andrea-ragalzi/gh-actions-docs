from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI()
todos = []


class TodoItem(BaseModel):
    id: int
    title: str
    completed: bool = False


@app.get(
    "/todos/",
    response_model=List[TodoItem],
    tags=["todos"],
    summary="Get all to-do items",
    description="Retrieve a list of all to-do items.",
)
def get_todos():
    return todos


@app.post(
    "/todos/",
    response_model=TodoItem,
    tags=["todos"],
    summary="Create a to-do item",
    description="Add a new to-do item to the list.",
)
def create_todo(todo: TodoItem):
    todos.append(todo)
    return todo


@app.put(
    "/todos/{todo_id}",
    response_model=TodoItem,
    tags=["todos"],
    summary="Update a to-do item",
    description="Update the details of a to-do item by its ID.",
)
def update_todo(todo_id: int, todo: TodoItem):
    for i, t in enumerate(todos):
        if t.id == todo_id:
            todos[i] = todo
            return todo
    raise HTTPException(status_code=404, detail="Todo not found")


@app.delete(
    "/todos/{todo_id}",
    tags=["todos"],
    summary="Delete a to-do item",
    description="Remove a to-do item by its ID.",
)
def delete_todo(todo_id: int):
    global todos
    todos = [t for t in todos if t.id != todo_id]
    return {"message": "Todo deleted"}
