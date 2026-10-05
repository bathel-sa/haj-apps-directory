FROM nginx:alpine

RUN apk add --no-cache gettext openssl

COPY nginx.conf.template /etc/nginx/nginx.conf.template
COPY entrypoint.sh /docker-entrypoint.d/10-generate-config.sh
RUN chmod +x /docker-entrypoint.d/10-generate-config.sh
