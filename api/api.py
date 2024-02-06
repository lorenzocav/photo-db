from typing import Any

import psycopg2
from fastapi import FastAPI

# Connect to your postgres DB
conn = psycopg2.connect(
    database="api_db", user="postgres", password="postgres", host="172.17.0.2"
)

# Open a cursor to perform database operations
cur = conn.cursor()

app = FastAPI()


@app.get("/")
def read_root() -> dict[str, str]:
    return {"Hello": "World"}


@app.get("/query")
def query() -> list[tuple[Any, ...]]:
    cur.execute("SELECT * FROM USER")
    return cur.fetchall()


@app.get("/items/{item_id}")
def read_item(item_id: int) -> dict[str, int]:
    return {"item_id": item_id}
