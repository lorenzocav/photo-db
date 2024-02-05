CREATE TABLE Persons (
    PersonID int,
    LastName varchar(255),
    FirstName varchar(255),
    Address varchar(255),
    City varchar(255)
);


-- CREATE TABLE IF NOT EXISTS user (
--     id serial PRIMARY KEY,
--     name varchar(255) NOT NULL
-- ),

-- CREATE TABLE IF NOT EXISTS photo (
--     id serial PRIMARY KEY,
--     photo_path varchar(255) NOT NULL,
--     date_upload bigint NOT NULL,
--     user_id serial REFERENCES cities(id) NOT NULL
-- );