FROM python:3.8.2-alpine as base


ENV PYTHONFAULTHANDLER=1 \
    PYTHONHASHSEED=random \
    PYTHONUNBUFFERED=1

WORKDIR /app

FROM base as final

ENV PIP_DEFAULT_TIMEOUT=100 \
    PIP_DISABLE_PIP_VERSION_CHECK=1 \
    PIP_NO_CACHE_DIR=1 \
    POETRY_VERSION=1.0.9

COPY . .

RUN apk update \
    && apk add postgresql-dev gcc python3-dev musl-dev libffi-dev

RUN pip install "poetry==$POETRY_VERSION" \
#     && python -m venv /venv \
    && poetry export --dev -f requirements.txt | pip install -r /dev/stdin

ENTRYPOINT ["/app/entrypoint.sh"]
