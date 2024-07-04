# Midterm Project - IS690 Summer 2024

- Local Commands
```
uvicorn main:app --reload
pytest
```

- Docker Commands
```
docker compose up --build -d
docker compose exec fastapi uvicorn main:app
docker compose exec fastapi pytest
```
