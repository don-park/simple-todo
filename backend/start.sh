#!/bin/sh
# start.sh
if [ -z "$BACKEND_PORT" ]; then
    echo "BACKEND_PORT is not set"
    exit 1
fi

# 숫자만 허용하는 정규식으로 검증
if ! echo "$BACKEND_PORT" | grep -qE '^[0-9]+$'; then
    echo "BACKEND_PORT must be a number"
    exit 1
fi

exec uvicorn app.main:app --host 0.0.0.0 --port "$BACKEND_PORT"