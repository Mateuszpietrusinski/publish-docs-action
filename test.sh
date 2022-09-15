#!/bin/bash

TIMESTAMP=$(date +%s)

docker build -t publish-docs-action:$TIMESTAMP -f Dockerfile .

docker run --rm \
    --entrypoint /bin/bash \
    publish-docs-action:$TIMESTAMP \
    -c "python3 -m pylint --rcfile /usr/src/publish-docs-action/.pylint.cfg /usr/src/farmer-instance-operator"

docker run --rm \
    --entrypoint /bin/bash \
    publish-docs-action:$TIMESTAMP \
    -c "python3 -m pytest -s ./tests/unit/"
