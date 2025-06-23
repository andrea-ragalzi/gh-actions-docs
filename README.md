# fastapi-medium-poetry

[![Python](https://img.shields.io/badge/python-3.12%2B-blue)]()
[![FastAPI](https://img.shields.io/badge/FastAPI-%3E%3D0.115.13<0.116.0-green)]()
[![Poetry](https://img.shields.io/badge/Poetry-%3E%3D1.0-yellow)]()
[![HTTPX](https://img.shields.io/badge/HTTPX-%3E%3D0.28.1-purple)]()

An example CRUD API for “to-do items” using **FastAPI**, managed and packaged with **Poetry**, and leveraging **HTTPX** for HTTP requests.

---

## Table of Contents

- [fastapi-medium-poetry](#fastapi-medium-poetry)
  - [Table of Contents](#table-of-contents)
  - [Project Metadata](#project-metadata)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
  - [Running the App](#running-the-app)
  - [API Endpoints](#api-endpoints)
  - [Development \& Testing](#development--testing)
  - [Project Structure](#project-structure)
  - [Contributing](#contributing)
  - [License](#license)

---

## Project Metadata

- **Name:** `fastapi-medium-poetry`  
- **Version:** `0.1.0`  
- **Description:** *A FastAPI CRUD example project managed with Poetry (Python ≥3.12), featuring HTTPX for HTTP calls.*  
- **Authors:** Andrea Ragalzi (<andrea.ragalzi.code@gmail.com>)  
- **Requires Python:** ≥ 3.12  
- **Dependencies:**  
  - `fastapi (>=0.115.13,<0.116.0)`  
  - `uvicorn[standard] (>=0.34.3,<0.35.0)`  
  - `httpx (>=0.28.1,<0.29.0)`

---

## Prerequisites

- **Python** 3.12 or higher  
- **Poetry** (for dependency & virtual-env management)  
- **Git** (to clone & version-control the repo)  

---

## Installation

1. **Clone the repo**  
   ```bash
   git clone https://github.com/<your-username>/fastapi-medium-poetry.git
   cd fastapi-medium-poetry
   ```

2. **Install dependencies**  
   ```bash
   poetry install
   ```

3. **Activate virtual environment** (optional)  
   ```bash
   poetry shell
   ```

---

## Running the App

Start the FastAPI server with automatic reload:

```bash
poetry run uvicorn main:app --reload
```

Then navigate to:

```
http://127.0.0.1:8000/docs
```

to explore the interactive Swagger UI.

---

## API Endpoints

| Method | Path            | Description                  |
| ------ | --------------- | ---------------------------- |
| **GET**    | `/todos/`      | List all to-do items         |
| **POST**   | `/todos/`      | Create a new to-do item      |
| **PUT**    | `/todos/{id}`  | Update an existing to-do item|
| **DELETE** | `/todos/{id}`  | Delete a to-do item          |

Payloads follow the Pydantic model `TodoItem` (fields: `id: int`, `title: str`, `completed: bool`).

---

## Development & Testing

- **Add dev dependencies** (e.g. pytest, pytest-cov):  
  ```bash
  poetry add --dev pytest pytest-cov
  ```

- **Run tests**:  
  ```bash
  poetry run pytest --cov
  ```

- **Run HTTPX-based integration tests** (if you write any):  
  ```bash
  poetry run pytest tests/
  ```

---

## Project Structure

```
fastapi-medium-poetry/
├── pyproject.toml
├── README.md
├── src/
│   └── fastapi_medium_poetry/
│       └── main.py
└── tests/
    └── test_api.py
```

- **`src/fastapi_medium_poetry/main.py`** – your FastAPI app with CRUD endpoints  
- **`tests/`** – place pytest test modules here  

---

## Contributing

1. Fork the repo  
2. Create a feature branch:  
   ```bash
   git checkout -b feature/awesome-new-feature
   ```  
3. Make your changes & add tests  
4. Commit and push to your fork  
5. Open a Pull Request for review  

---

## License

This project is licensed under the **MIT License**. See [LICENSE](LICENSE) for details.