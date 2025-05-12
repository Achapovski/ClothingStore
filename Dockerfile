FROM python:3.12.0

ENV HOME=/home/FastAPI \
    APP_HOME=/home/FastAPI/app \
    PYTHONPATH="$PYTHONPATH:/home/FastAPI" \
    PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1

RUN mkdir -p $APP_HOME && groupadd -r fastgroup && useradd -r -g fastgroup fast
WORKDIR $HOME

COPY poetry.lock pyproject.toml $HOME

RUN pip install poetry
RUN poetry config virtualenvs.create false
RUN poetry install --no-root

COPY app $APP_HOME

USER fast
