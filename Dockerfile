FROM debian:stable-slim

RUN apt update \
  && apt -y install coreutils

COPY entrypoint.sh /entrypoint.sh

ENTRYPOINT ["/entrypoint.sh"]
