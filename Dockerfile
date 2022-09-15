FROM python:3.10-slim

WORKDIR /usr/src/publish-docs-action

COPY Pipfile Pipfile.lock ./

RUN pip install --progress-bar off pipenv && pipenv install --system

COPY . .

COPY entrypoint.sh /entrypoint.sh

ENTRYPOINT ["/entrypoint.sh"]
