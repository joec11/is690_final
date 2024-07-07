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

## Source Code and Data References

- Source Code References
    - GitHub
        - https://github.com/pixegami/langchain-rag-tutorial
    - Youtube
        - https://www.youtube.com/watch?v=tcqEUSNCn8I
<p>

- txt file (data/market_overview.txt)
    - Generated from ChatGPT.
<p>

- csv file (data/constituents.csv)
    - https://github.com/datasets/s-and-p-500-companies/blob/main/data/constituents.csv
