# API Reference

Tutti gli endpoint restituiscono o accettano JSON secondo il modello Pydantic `TodoItem`.

| Method | Path           | Description               |
| ------ | -------------- | ------------------------- |
| GET    | `/todos/`      | List all to-do items      |
| POST   | `/todos/`      | Create a new to-do item   |
| PUT    | `/todos/{id}`  | Update an existing to-do  |
| DELETE | `/todos/{id}`  | Delete a to-do item       |
