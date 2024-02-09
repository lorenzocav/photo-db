FROM python:3.11

WORKDIR /api

COPY requirements.txt /api/requirements.txt

RUN pip install --no-cache-dir -r /api/requirements.txt

COPY ./api.py /api/

CMD ["uvicorn", "api:app", "--host", "0.0.0.0", "--port", "8000"]
