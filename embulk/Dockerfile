FROM openjdk:8-jre-alpine

ARG EMBULK_VER=${EMBULK_VER:-"0.9.23"}

RUN apk --update add --virtual build-dependencies curl \
    && curl --create-dirs -o ~/.embulk/bin/embulk -L "https://dl.embulk.org/embulk-${EMBULK_VER}.jar" \
    && chmod +x ~/.embulk/bin/embulk \
    && apk del build-dependencies
RUN apk --update add libc6-compat

RUN apk add --update --no-cache python3 && ln -sf python3 /usr/bin/python
RUN pip3 install pyyaml

COPY ./converter.py /converter.py
COPY entrypoint.sh /entrypoint.sh

ENTRYPOINT ["sh", "/entrypoint.sh"]
