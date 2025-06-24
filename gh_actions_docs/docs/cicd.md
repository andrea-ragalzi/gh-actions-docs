# CI/CD Pipeline

La pipeline GitHub Actions è definita in `.github/workflows/ci.yml` e fa:

1. Setup ambiente Python  
2. Installazione dipendenze con Poetry  
3. Esecuzione linting (flake8, black)  
4. Esecuzione test (pytest)  
5. Build e deploy della docs con `mkdocs gh-deploy` su push su `main`