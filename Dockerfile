FROM python:3
ENV PYTHONUNBUFFERED=1 \
    PIP_NO_CACHE_DIR=off \
    PIP_DISABLE_PIP_VERSION_CHECK=on \
    PIP_DEFAULT_TIMEOUT=100 \

    POETRY_VERSION=1.0.5 \
    POETRY_VIRTUALENVS_CREATE=false \
    POETRY_CACHE_DIR='/var/cache/pypoetry'
WORKDIR /dataox
COPY poetry.lock pyproject.toml /dataox/
RUN pip install poetry
RUN poetry install
COPY . .
