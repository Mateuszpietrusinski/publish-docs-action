#!/bin/bash

X_USER_ID=$1
X_API_KEY=$2
DOC_NAME=$3
DOC_IMAGE_TAG=$4
DOC_IMAGE=$5
DOC_PATH=$6
DOC_PORT=$7
DOC_HAS_BASE_PATH=$8

DOC_INSTANCE_NAMESPACE=

echo $X_USER_ID

ls -al ~/

# whereis env

env

curl -I -X GET https://google.com/

curl -H X-User-Id: "$X_USER_ID'  -H "X-Api-Key: $X_API_KEY" -H "Content-Type: application/json" -X GET https://farmer.storefrontcloud.io/instance/docs-europe-west1-gcp-storefrontcloud-io

# curl -H X-User-Id: "$X_USER_ID'  -H "X-Api-Key: $X_API_KEY" -H 'Content-Type: application/json' -X PATCH -d '
  # {
  #   "additional_apps":{
  #     "apps":[{
  #       "name":"docs-v2-bigcommerce",
  #       "tag":"${{ steps.get_version.outputs.VERSION }}",
  #       "image":"registry.storefrontcloud.io/docs-storefrontcloud-io/v2-bigcommerce",
  #       "path":"/bigcommerce",
  #       "port":"80"
  #     }]
  #   }
  # }' https://farmer.storefrontcloud.io/instance/docs-europe-west1-gcp-storefrontcloud-io



time=$(date)
echo "::set-output name=time::$time"
