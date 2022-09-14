FROM debian:slim

RUN apt update \
  && apt -y install coreutils

COPY entrypoint.sh /entrypoint.sh

ENTRYPOINT ["/entrypoint.sh"]
