#!/bin/sh

BACKEND_URL=${BACKEND_URL}

echo "-----------------------------------------------------" | tee -a ~/log.txt
echo `date` | tee -a ~/log.txt
stop=true
test_result=$(speedtest-cli --json --secure --no-pre-allocate)

if echo "$test_result" | grep -qe '{*}'
then
    stop=false
else
    test_result=$(speedtest-cli --json --secure --no-pre-allocate)
    if echo "$test_result" | grep -qe '{*}'
        then
            stop=false
    fi
fi

echo | tee -a ~/log.txt
echo "Speedtest result: $test_result" | tee -a ~/log.txt
echo | tee -a ~/log.txt

if $stop
then
    exit 1
fi

echo "$BACKEND_URL" | tee -a ~/log.txt

wget -S "$BACKEND_URL" --header='Content-Type: application/json' -O- \
    --post-data="$test_result" 2>&1 \
    | tee -a ~/log.txt
echo `date` | tee -a ~/log.txt
