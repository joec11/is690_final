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

- View the Application RAG HTML Page in a Web Browser:
```
localhost:8000
```

- View the Application Routes in a Web Browser:
```
localhost:8000/docs
```

- Terminate the Application from the Terminal:
```
Type Control-C (^C)
```

## Presentation
[IS690 Final Project Presentation](https://youtu.be/sYmmKKIgtA0)

## Source Code and Data References

- Source Code References:
    - [GitHub - pixegami](https://github.com/pixegami/langchain-rag-tutorial)
    - [Youtube - pixegami -- RAG + Langchain Python Project: Easy AI/Chat For Your Docs](https://www.youtube.com/watch?v=tcqEUSNCn8I)
<p>

- txt files
    - (Generated from ChatGPT):
        - data/economic_market_overview_August_2024.txt
        - data/market_overview.txt
        - data/political_news_crypto_August_2024.txt
        - data/top_twenty_cryptocurrencies.txt
        - data/top_twenty_stocks.txt
    
    - (Online News Sources):
        - data/apnews_Dow_News_August_02_2024.txt
            - [AP News - Dow News - August 02, 2024](https://apnews.com/article/stocks-markets-rates-yen-inflation-20ce445cdd86be98fb3682a33e88442b#)
        
        - data/cnbc_ethereum_etfs_news_July_25_2024.txt
            - [CNBC - Ethereum ETFs News - July, 25, 2024](https://www.cnbc.com/2024/07/25/why-the-new-spot-ether-etfs-may-be-a-hit-despite-recent-weakness.html)
<p>
