FROM python:3.10

RUN pip install poetry

WORKDIR /app

COPY . /app

RUN poetry install

ENTRYPOINT [ "./entrypoint.sh" ]