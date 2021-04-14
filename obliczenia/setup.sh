#!/usr/bin/env bash

set -o errexit -o pipefail -o nounset


declare -r PORT="${PORT-1337}"

echo >&2 "Listening on port ${PORT}..."
exec socat tcp-l:"$PORT",reuseaddr,fork exec:./main.py
