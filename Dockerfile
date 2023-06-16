FROM python:3.10

RUN pip install poetry

WORKDIR /app

COPY . /app

RUN poetry install

RUN chmod +x entrypoint.sh

ENTRYPOINT [ "./entrypoint.sh" ]