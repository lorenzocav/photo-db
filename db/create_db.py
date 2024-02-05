import sqlite3


def create_db(conn: sqlite3.Connection, cursor: sqlite3.Cursor) -> None:
    # Create the USER table
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS USER (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL
        )
    """
    )

    # Create the PHOTO table
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS PHOTO (
            id INTEGER PRIMARY KEY,
            photo TEXT NOT NULL,
            date_upload INTEGER NOT NULL,
            user_id INTEGER,
            FOREIGN KEY (user_id) REFERENCES USER(id)
        )
    """
    )

    # Commit the changes
    conn.commit()


if __name__ == "__main__":
    # Connect to the database (creates a new database if it doesn't exist)
    conn = sqlite3.connect("photo.db")
    cursor = conn.cursor()
    create_db(conn, cursor)

    # Close the connection
    conn.close()
