FROM python:3.11-slim-buster

COPY ./requirements.txt /app/

WORKDIR /app

RUN pip install -r requirements.txt

COPY . /app

EXPOSE 8080

# ENTRYPOINT ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8080" " --env-file" ".env.dev"]

CMD uvicorn app.main:app --host 0.0.0.0 --port 8080 --reload --env-file .env.dev
