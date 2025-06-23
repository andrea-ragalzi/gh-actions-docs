# gh-actions-docs

[![Python](https://img.shields.io/badge/python-3.12%2B-blue)]()  
[![FastAPI](https://img.shields.io/badge/FastAPI-%3E%3D0.115.13<0.116.0-green)]()  
[![Poetry](https://img.shields.io/badge/Poetry-%3E%3D1.0-yellow)]()  
[![HTTPX](https://img.shields.io/badge/HTTPX-%3E%3D0.28.1-purple)]()  
[![GitHub Actions](https://img.shields.io/badge/CI%2FCD-GitHub%20Actions-orange)]()  
[![Docs](https://img.shields.io/badge/docs-MkDocs-blue)]()

An example CRUD API for “to-do items” using **FastAPI**, packaged with **Poetry**, leveraging **HTTPX**, automated via **GitHub Actions**, and documented with **MkDocs** on GitHub Pages.

---

## Table of Contents

- [gh-actions-docs](#gh-actions-docs)
  - [Table of Contents](#table-of-contents)
  - [Project Metadata](#project-metadata)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
  - [Running the Application](#running-the-application)
  - [API Endpoints](#api-endpoints)
  - [Documentation](#documentation)
  - [CI/CD Pipeline](#cicd-pipeline)
  - [Development \& Testing](#development--testing)
  - [Project Structure](#project-structure)
  - [Contributing](#contributing)
  - [License](#license)

---

## Project Metadata

- **Name:** `gh-actions-docs`  
- **Version:** `0.1.0`  
- **Description:** *FastAPI CRUD example managed with Poetry (Python ≥3.12), using HTTPX, continuous integration via GitHub Actions, and documentation hosted on GitHub Pages with MkDocs.*  
- **Authors:** Andrea Ragalzi (<andrea.ragalzi.code@gmail.com>)  
- **Python Requirement:** ≥ 3.12  
- **Dependencies:**  
  - `fastapi (>=0.115.13,<0.116.0)`  
  - `uvicorn[standard] (>=0.34.3,<0.35.0)`  
  - `httpx (>=0.28.1,<0.29.0)`

---

## Prerequisites

- **Python** 3.12 or newer installed on your system  
- **Poetry** for virtual environment and dependency management  
- **Git** to clone and version-control the repository  
- **GitHub account** to use GitHub Actions and GitHub Pages

---

## Installation

1. **Clone the repository**  
   ```bash
   git clone https://github.com/<your-username>/gh-actions-docs.git
   cd src/gh-actions-docs
   ```

2. **Install dependencies** via Poetry  
   ```bash
   poetry install
   ```

3. **Activate the virtual environment** (optional)  
   ```bash
   poetry env activate
   ```

---

## Running the Application

Start the development server with live reload:

```bash
poetry run uvicorn main:app --reload
```

Then open your browser at:

```
http://127.0.0.1:8000/docs
```

---

## API Endpoints

| Method | Path           | Description               |
| ------ | -------------- | ------------------------- |
| GET    | `/todos/`      | List all to-do items      |
| POST   | `/todos/`      | Create a new to-do item   |
| PUT    | `/todos/{id}`  | Update an existing to-do  |
| DELETE | `/todos/{id}`  | Delete a to-do item       |

All endpoints follow the Pydantic model `TodoItem` (`id: int`, `title: str`, `completed: bool`).

---

## Documentation

The project uses **MkDocs** to generate a static documentation site from Markdown files.

- Customize `mkdocs.yml` in the repo root to configure site title, theme, and navigation.  
- Write docs under the `docs/` directory (e.g., `docs/index.md`, `docs/installation.md`).  

To build and preview locally:

```bash
mkdocs serve
```

To deploy to **GitHub Pages**:

```bash
mkdocs gh-deploy
```

Your documentation will be published on:

```
https://<your-username>.github.io/gh-actions-docs/
```

---

## CI/CD Pipeline

The GitHub Actions workflow at `.github/workflows/ci.yml` includes steps to:  
1. Setup Python environment  
2. Install dependencies via Poetry  
3. Run linting (e.g., `flake8`, `black`)  
4. Execute tests (`pytest`)  
5. Build and deploy documentation with `mkdocs gh-deploy` on push to `main`.

---

## Development & Testing

- **Add or update dev dependencies** (e.g., pytest, pytest-cov):  
  ```bash
  poetry add --dev pytest pytest-cov
  ```
- **Run tests** with coverage reporting:  
  ```bash
  poetry run pytest --cov
  ```

---

## Project Structure

```plaintext
gh-actions-docs/
├── docs/                   # MkDocs markdown files
│   ├── index.md
│   └── installation.md
├── src/
│   └── main.py             # FastAPI application
├── .github/
│   └── workflows/
│       └── ci.yml          # CI/CD workflow
├── mkdocs.yml              # MkDocs configuration
├── pyproject.toml
└── README.md
```

---

## Contributing

1. Fork the repository  
2. Create a branch:  
   ```bash
   git checkout -b feature/awesome-addition
   ```  
3. Make your changes and add tests  
4. Commit and push to your fork  
5. Open a Pull Request for review

---

## License

This project is licensed under the **MIT License**. See [LICENSE](LICENSE) for details.