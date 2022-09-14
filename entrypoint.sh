#!/bin/bash

X_USER_ID=$1
X_API_KEY=$2
DOC_NAME=$3
DOC_IMAGE_TAG=$4
DOC_IMAGE=$5
DOC_PATH=$6
DOC_PORT=$7
DOC_HAS_BASE_PATH=$8

echo $X_USER_ID

ls -al ~/

# whereis env

env

curl -I -X GET https://google.com/


time=$(date)
echo "::set-output name=time::$time"
