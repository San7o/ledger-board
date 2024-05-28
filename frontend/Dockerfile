FROM node:22-bookworm

WORKDIR /home/docker/app

RUN rm -rf .angular/cache

RUN useradd -r -g users docker
USER docker

CMD ["npm", "start"]

EXPOSE 4200
