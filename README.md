# Photo-DB
A service that stores photos

## Development

### Installing dependencies
First install the poetry package manager at [https://python-poetry.org/docs/](https://python-poetry.org/docs/).

Then simply run 
```bash
poetry install --with=api,dev --no-root
```
This command creates a virtual environment with the dependencies present in the pyproject.toml file

### Running the container
```bash
poetry export -f requirements.txt --with=api -o ./api/requirements.txt;
docker compose build;
docker compose up
```
