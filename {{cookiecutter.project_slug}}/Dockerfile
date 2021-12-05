FROM python:3.10-slim-bullseye

RUN apt-get update && apt-get install curl build-essential -y

WORKDIR /app/

# Install Poetry
RUN curl -sSL https://install.python-poetry.org/install-poetry.py | python - && \
  cd /usr/local/bin && \
  ln -s /root/.local/bin/poetry && \
  poetry config virtualenvs.create false

COPY ./pyproject.toml ./poetry.lock /app/
RUN poetry install --no-root --no-dev

COPY ./start.sh .
RUN chmod +x ./start.sh

COPY ./gunicorn_conf.py .

COPY ./start-reload.sh .
RUN chmod +x ./start-reload.sh

COPY ./app ./app

EXPOSE 80

CMD ["./start.sh"]
