# Midterm Project - IS690 Summer 2024

- Local Commands:
```
uvicorn main:app --reload
pytest
```

- Docker Commands:
```
docker compose up --build -d
docker compose exec fastapi uvicorn main:app
docker compose exec fastapi pytest
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
[IS690 Midterm Presentation](https://youtu.be/r0UDExgA0OE)

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
