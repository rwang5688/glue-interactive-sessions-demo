#!/bin/bash
# set env var
. ./env.sh

PROGRAM=$(basename $0)

usage() {
  echo "Usage: $PROGRAM [config.json]"
  echo "If parameter exists, use specified manifest.  Otherise, use config.json in current working directory."
}

usage_and_exit()
{
    usage
    exit $1
}

error()
{
    echo "$@" 1>&2
    usage_and_exit 1
}

if [ $# -eq 0 ]; then
  config_json="config.json"
else
  config_json=$1
fi

if [ ! -f $config_json ]; then
  error "$config_json file does not exist."
fi

# delete glue sessions that have been provisioned
echo "[CMD] python3 ./delete_glue_sessions.py $config_json"
python3 ./delete_glue_sessions.py $config_json

