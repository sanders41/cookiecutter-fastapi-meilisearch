FROM python:3.10-slim-bullseye

RUN useradd --create-home appuser

WORKDIR /home/appuser

RUN apt-get update && apt-get install curl build-essential -y

EXPOSE 80

# Install Poetry
RUN curl -sSL https://install.python-poetry.org | POETRY_HOME=/etc/poetry python3 - && \
  cd /usr/local/bin && \
  ln -s /etc/poetry/bin/poetry

COPY ./start.sh ./
RUN chmod +x ./start.sh

USER appuser

COPY ./gunicorn_conf.py ./

COPY ./app ./app

COPY ./pyproject.toml ./poetry.lock ./

RUN poetry run python -m pip install -U pip
RUN poetry install --no-root --no-dev

CMD ["./start.sh"]
