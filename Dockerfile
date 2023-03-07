# syntax=docker/dockerfile:1

FROM python:3.9-slim-buster

ENV POETRY_VERSION=1.1.13 \
    POETRY_VIRTUALENVS_CREATE=false
ENV http_proxy=http://proxy.fpt.vn:80
ENV https_proxy=https://proxy.fpt.vn:80
ENV HTTP_PROXY=http://proxy.fpt.vn:80
ENV HTTPS_PROXY=https://proxy.fpt.vn:80
ENV no_proxy=172.27.230.14,localhost,127.0.0.1


# Install poetry
RUN pip install "poetry==$POETRY_VERSION"

# Copy only requirements to cache them in docker layer
WORKDIR /flask_app
COPY poetry.lock pyproject.toml /flask_app/

# Project initialization:
RUN poetry install --no-interaction --no-ansi --no-root --no-dev

# Copy Python code to the Docker image
COPY app /flask_app/app/
#COPY migrations /flask_app/migrations
COPY scripts /flask_app/scripts
COPY tests /flask_app/tests
COPY run_app.py /flask_app/
COPY .env /flask_app/

RUN ./scripts/initialize_project.sh
RUN poetry update
RUN chmod +x /flask_app/deploy_dev.sh

CMD ["./scripts/deploy_dev.sh"]