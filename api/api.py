from typing import Annotated, Optional, Sequence

from fastapi import FastAPI
from pydantic import StringConstraints
from sqlmodel import Field, Session, SQLModel, create_engine, select


class Account(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: Annotated[str, StringConstraints(max_length=255)]


class Photo(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    photo_path: Annotated[str, StringConstraints(max_length=63)]
    photo_title: Annotated[str, StringConstraints(max_length=63)]
    date_upload: int
    user_id: int


SQLALCHEMY_DATABASE_URL = "postgresql://postgres:postgres@db-container:5432/api_db"
engine = create_engine(SQLALCHEMY_DATABASE_URL)

app = FastAPI()


@app.post("/account", status_code=201)
def insert_account(account: Account) -> Account:
    with Session(engine) as session:
        session.add(account)
        session.commit()
        session.refresh(account)

    return account


@app.get("/accounts")
def get_accounts() -> Sequence[Account]:
    with Session(engine) as session:
        accounts = session.exec(select(Account)).all()

    return accounts


@app.get("/account/{account_id}")
def get_account_name(account_id: int) -> str:
    with Session(engine) as session:
        statement = select(Account.name).where(Account.id == account_id)
        name = session.exec(statement).one()

    return name


@app.delete("/account/{account_id}")
def delete_account(account_id: int) -> None:
    with Session(engine) as session:
        statement = select(Account).where(Account.id == account_id)
        results = session.exec(statement)
        account = results.one()

        session.delete(account)
        session.commit()


@app.put("/account")
def update_account(account: Account) -> Account:
    with Session(engine) as session:
        statement = select(Account).where(Account.id == account.id)
        results = session.exec(statement)
        old_account = results.one()

        old_account.name = account.name
        session.add(old_account)
        session.commit()
        session.refresh(old_account)

    return old_account
