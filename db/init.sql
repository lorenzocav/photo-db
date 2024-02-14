CREATE TABLE IF NOT EXISTS account (
    id serial PRIMARY KEY,
    name varchar(255) NOT NULL
);

CREATE TABLE IF NOT EXISTS photo (
    id serial PRIMARY KEY,
    photo_title varchar(64) NOT NULL,
    photo_data_base64 TEXT,
    date_upload bigint NOT NULL,
    user_id serial REFERENCES account(id) NOT NULL
);