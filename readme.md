# Final Project - IS690 Summer 2024

- Local Commands:
```
uvicorn app.main:app --reload
pytest --pylint --cov
```

- Docker Commands:
```
docker compose up --build -d
docker compose exec fastapi uvicorn app.main:app
docker compose exec fastapi pytest --pylint --cov
docker compose down
```

- View the Application in a Web Browser:
```
localhost:8000/docs
```

- Terminate the Application from the Terminal:
```
Type Control-C (^C)
```

## Presentation

## Source Code and Data References

- Source Code References:
    - GitHub:
        - https://github.com/pixegami/langchain-rag-tutorial
    - Youtube:
        - https://www.youtube.com/watch?v=tcqEUSNCn8I
<p>

- txt files (Generated from ChatGPT):
    - data/market_overview.txt
    - data/top_twenty_cryptocurrencies.txt
    - data/top_twenty_stocks.txt
<p>
