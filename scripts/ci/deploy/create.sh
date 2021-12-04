#!/bin/bash

set -euo pipefail

if [ "$#" -ne 2 ]; then
    echo "Invalid number of arguments"
    echo "./scripts/ci/deploy/create.sh <service> <tag>"
    exit 1
fi

SERVICE="$1"
TAG="$2"

env_prefix="$(echo ${SERVICE}- | awk '{print toupper($0)}' | sed 's/-/_/g')"
env_variables="$(printenv | { grep "${env_prefix}" || test $? = 1; } | sed "s/^${env_prefix}//g")"

content="$(./scripts/ci/yaml/merge.sh ./src/${SERVICE}/k8s)"

content="$(echo "${content}" | sed "s/{{IMAGE_TAG}}/${TAG}/g")"

for variable in ${env_variables}; do
    variable_key="$(echo "${variable}" | cut -d '=' -f1)"
    variable_value="$(echo "${variable}" | cut -d '=' -f2-)"
    content="$(echo "${content}" | sed "s/{{${variable_key}}}/${variable_value}/g")"
done

echo "${content}"
