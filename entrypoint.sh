#!/bin/bash

X_USER_ID=$1
X_API_KEY=$2
DOC_NAME=$3
DOC_IMAGE_TAG=$4
DOC_IMAGE=$5
DOC_PATH=$6
DOC_PORT=$7
DOC_HAS_BASE_PATH=$8

if [[ -z "$X_USER_ID" ]]; then
    echo -e "\x1B[31m Set variable user-id";
    exit 1
fi

if [[ -z "$X_API_KEY" ]]; then
    echo -e "\x1B[31m Set variable api-key";
    exit 1
fi

if [[ -z "$DOC_NAME" ]]; then
    echo -e "\x1B[31m Set variable name";
    exit 1
fi

if [[ -z "$DOC_IMAGE_TAG" ]]; then
    echo -e "\x1B[31m Set variable tag";
    exit 1
fi

if [[ -z "$DOC_IMAGE" ]]; then
    echo -e "\x1B[31m Set variable image";
    exit 1
fi

if [[ -z "$DOC_PATH" ]]; then
    echo -e "\x1B[31m Set variable path";
    exit 1
fi

if [[ -z "$DOC_PORT" ]]; then
    echo -e "\x1B[31m Set variable port";
    exit 1
fi

./publish_docs.py -u $X_USER_ID -a $X_API_KEY -n $DOC_NAME -t $DOC_IMAGE_TAG -i $DOC_IMAGE -p $DOC_PATH -r $DOC_PORT -s "$DOC_HAS_BASE_PATH"
