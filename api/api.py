from typing import Annotated, Optional, Sequence

from fastapi import FastAPI, HTTPException
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
        name = session.exec(statement).first()
        if name is None:
            raise HTTPException(
                status_code=404, detail=f"Account with id: {id} not found"
            )

    return name


@app.delete("/account/{account_id}", status_code=204)
def delete_account(account_id: int) -> None:
    with Session(engine) as session:
        statement = select(Account).where(Account.id == account_id)
        account = session.exec(statement).first()
        if account is None:
            raise HTTPException(
                status_code=404, detail=f"Account with id: {id} not found"
            )

        session.delete(account)
        session.commit()


@app.put("/account")
def update_account(account: Account) -> Account:
    with Session(engine) as session:
        statement = select(Account).where(Account.id == account.id)
        old_account = session.exec(statement).first()
        if old_account is None:
            raise HTTPException(
                status_code=404, detail=f"Account with id: {id} not found"
            )

        session.add(account)
        session.commit()
        session.refresh(account)

    return account
