FROM python:3.10-slim-bullseye

WORKDIR /app/

RUN apt-get update && apt-get install curl build-essential -y

# Install Poetry
RUN curl -sSL https://install.python-poetry.org/install-poetry.py | python - && \
  cd /usr/local/bin && \
  ln -s /root/.local/bin/poetry && \
  poetry config virtualenvs.create true

RUN poetry run python -m pip install -U pip

COPY ./pyproject.toml ./poetry.lock /app/
RUN poetry install --no-root --no-dev

COPY ./start.sh .
RUN chmod +x ./start.sh

COPY ./gunicorn_conf.py .

COPY ./app ./app

EXPOSE 80

CMD ["./start.sh"]
