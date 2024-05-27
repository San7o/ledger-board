FROM nikolaik/python-nodejs:python3.11-nodejs22

WORKDIR /app/frontend

COPY ./backend/requirements.txt /tmp
RUN groupadd -r docker && useradd -r -g docker docker
RUN python3 -m pip install -r /tmp/requirements.txt

USER docker

CMD ["npm", "start"]

EXPOSE 4200 4200
EXPOSE 8000 8000
