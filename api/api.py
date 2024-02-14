from enum import Enum
from typing import Annotated, Optional, Sequence

from fastapi import FastAPI, HTTPException, Path, Query, UploadFile
from fastapi.middleware.cors import CORSMiddleware
from pydantic import StringConstraints
from sqlmodel import Field, Session, SQLModel, create_engine, select


class Account(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: Annotated[str, StringConstraints(max_length=255)]


class Photo(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    # photo_path: Annotated[str, StringConstraints(max_length=63)]
    photo_title: Annotated[str, StringConstraints(max_length=63)]
    photo_data: bytes
    date_upload: int
    user_id: int


class Tags(Enum):
    account = "account"
    photo = "photo"


SQLALCHEMY_DATABASE_URL = "postgresql://postgres:postgres@db-container:5432/api_db"
engine = create_engine(SQLALCHEMY_DATABASE_URL)

app = FastAPI()
# Allow all origins for CORS (be cautious in production)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.post(
    "/account",
    status_code=201,
    description="Route to create Account row",
    tags=[Tags.account],
)
def insert_account(account: Account) -> Account:
    with Session(engine) as session:
        session.add(account)
        session.commit()
        session.refresh(account)

    return account


@app.get(
    "/accounts",
    status_code=200,
    description="Route to get Account Table view",
    tags=[Tags.account],
)
def get_accounts() -> Sequence[Account]:
    with Session(engine) as session:
        accounts = session.exec(select(Account)).all()

    return accounts


@app.get(
    "/account/{account_id}",
    status_code=200,
    description="Route to get an account by its id",
    tags=[Tags.account],
)
def get_account_name(
    account_id: int = Path(..., title="The id of the account to get", gt=0),
) -> str:
    with Session(engine) as session:
        statement = select(Account.name).where(Account.id == account_id)
        name = session.exec(statement).first()
        if name is None:
            raise HTTPException(
                status_code=404, detail=f"Account with id: {id} not found"
            )

    return name


@app.delete(
    "/account/{account_id}",
    status_code=204,
    description="Route to delete an account by its id",
    tags=[Tags.account],
)
def delete_account(
    account_id: int = Path(..., title="The id of the account to delete", gt=0),
) -> None:
    with Session(engine) as session:
        statement = select(Account).where(Account.id == account_id)
        account = session.exec(statement).first()
        if account is None:
            raise HTTPException(
                status_code=404, detail=f"Account with id: {id} not found"
            )

        session.delete(account)
        session.commit()


@app.put(
    "/account",
    status_code=200,
    description="Route to update an existing account",
    tags=[Tags.account],
)
def update_account(account: Account) -> Account:
    with Session(engine) as session:
        statement = select(Account).where(Account.id == account.id)
        existing_account = session.exec(statement).first()

        if existing_account is None:
            raise HTTPException(
                status_code=404, detail=f"Account with id: {account.id} not found"
            )

        existing_account.name = account.name
        session.commit()
        session.refresh(existing_account)

    return existing_account


@app.post(
    "/photo", status_code=201, description="Route to upload a photo", tags=[Tags.photo]
)
async def upload_photo(
    photo: UploadFile,
    account_id: int = Query(
        ..., description="The id of the account associated with the photo"
    ),
) -> dict[str, str]:
    if photo.content_type.split("/")[0] != "image":
        raise HTTPException(status_code=422, detail="The uploaded file is not an image")

    photo_data = await photo.read()

    with Session(engine) as session:
        photo_db = Photo(
            photo_title=photo.filename,
            photo_data=photo_data,
            date_upload=123456,
            user_id=account_id,
        )
        session.add(photo_db)
        session.commit()
        session.refresh(photo_db)

    return {"message": "Photo uploaded successfully"}
