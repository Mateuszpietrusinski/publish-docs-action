#!/bin/bash

X_USER_ID=$1
X_API_KEY=$2
NAME=$3
TAG=$4
IMAGE=$5
PATH=$6
PORT=$7
HAS_BASE_PATH=$8

echo $X_USER_ID

env

time=$(date)
echo "::set-output name=time::$time"
