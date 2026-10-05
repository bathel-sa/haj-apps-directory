#!/bin/sh
set -e

SERVER_NAME="${SERVER_NAME:-localhost}"
export SERVER_NAME

envsubst '${SERVER_NAME}' < /etc/nginx/nginx.conf.template > /etc/nginx/nginx.conf

if [ ! -s /etc/nginx/certs/fullchain.pem ] || [ ! -s /etc/nginx/certs/privkey.pem ]; then
    echo "No valid certificates found in /etc/nginx/certs - generating self-signed certificate for ${SERVER_NAME}"
    mkdir -p /etc/nginx/certs
    SAN_HOST=$(echo "${SERVER_NAME}" | awk '{print $1}')
    openssl req -x509 -nodes -newkey rsa:2048 \
        -keyout /etc/nginx/certs/privkey.pem \
        -out /etc/nginx/certs/fullchain.pem \
        -days 825 \
        -subj "/CN=${SERVER_NAME}" \
        -addext "subjectAltName=DNS:${SAN_HOST}"
    chmod 644 /etc/nginx/certs/fullchain.pem
    chmod 600 /etc/nginx/certs/privkey.pem
else
    echo "Using mounted certificates from /etc/nginx/certs"
fi
