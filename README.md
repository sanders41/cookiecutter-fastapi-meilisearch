# Cookiecutter FastAPI MeiliSearch

[![Tests Status](https://github.com/sanders41/cookiecutter-fastapi-meilisearch/workflows/Testing/badge.svg?branch=main&event=push)](https://github.com/sanders41/cookiecutter-fastapi-meilisearch/actions?query=workflow%3ATesting+branch%3Amain+event%3Apush)
[![pre-commit.ci status](https://results.pre-commit.ci/badge/github/sanders41/cookiecutter-fastapi-meilisearch/main.svg)](https://results.pre-commit.ci/latest/github/sanders41/cookiecutter-fastapi-meilisearch/main)

Cookiecutter template to start a FastAPI project with MeiliSearch built in.

## Whats included

- FastAPI project structure setup for use with [Poetry](https://python-poetry.org/)
- Routes built and ready for interacting with MeiliSearch
- [camel-converter](https://github.com/sanders41/camel-converter) to automatically convert to and
  from camel case when serializing and deserializing data.
- Options for using docker as a stand alone for the project or docker-compose to also start a
  MeiliSearch server.

## Dev dependencies that are included

- black
- flake8
- httpx
- isort
- mypy
- pre-commit
- pytest
- pytest-asyncio
- pytest-cov
- tox

## How to use

First make sure you have cookiecutter installed. Instructions for installing can be found [here](https://cookiecutter.readthedocs.io/en/1.7.2/installation.html).

Once cookiecutter is installed go to the directory where you want to create the project and run:

```zsh
cookiecutter https://github.com/sanders41/cookiecutter-fastapi-meilisearch
```

You will be asked to fill in the following information:

- project_name: The name of the project
- project_slug: The development friendly name of the project. By default, based on the project name
- project_description: A short discription of the purpose of the project [Optional]
- creator: The full name of the project creator
- creator_email: The email address for the creator
- license: The license to use for the project. Select "No license" if no license should be included
- copyright_year: The year to use for the copyright year in the license file. Required for MIT and GNU General Public License v3.0 licenses
- python_version: The version of Python that can be used for the project. By default 3.10 will be used.
- tox_python_version: The version of Python that tox should use for testing. By default py38, py39 is used
- max_line_length: The maximum allowed line length. By default 100 is used
- use_dependabot: Adds a GitHub action for dependabot: Default = True
- use_release_drafter: Adds GitHub action to automatically generate change logs. Default = True
- meilisearch_url: The URL for the MeiliSearch instance. Note: if the url is `localhost` and the provided
  docker-compose file is being used set this value to `https://meilisearch:7700`.
- meilisearch_api_key: The API key for the MeiliSearch instance

Next install the dependencies

```sh
poetry install
```

Create a git repositry

```zsh
git init
```

Install the pre-commit hooks

```zsh
pre-commit install
```

Commit the files to git

```zsh
git add .
git commit -am 'Inital commit'
```

Now the project is ready to use.

## Docker

There is an option to use Docker with just the FastAPI project, or docker-compose to combine both
the FastAPI project and the MeiliSearch server.

For Docker build the project

```sh
docker build . -t fastapi-meilisearch
```

Before starting the container make sure MeiliSearch is running. Then run it with:

```sh
docker run --rm -p 80:80 fastapi-meilisearch:latest
```

For docker-compose build the project

```sh
docker-compose build
```

Then start it with.

```sh
docker-compose up
```

The docker-compose option will also start a MeiliSearch instance so there is no need to start one
on your own.

## Contributing

Contributions to this project are welcome. If you are interesting in contributing please see our [contributing guide](CONTRIBUTING.md)
