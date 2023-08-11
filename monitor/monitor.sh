#!/bin/sh

payload=$(speedtest-cli --json | tee -a /log.txt)
echo "Payload: $payload"
wget -S "${BACKEND_HOST}:${BACKEND_PORT}${BACKEND_URL}" --header='Content-Type: application/json' -O- \
    --post-data="$payload" 2>&1 \
    | tee -a /log.txt