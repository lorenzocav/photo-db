# Use the official Postgres base image
FROM postgres:16

# Copy the SQL script into the container
COPY init.sql /docker-entrypoint-initdb.d/
