FROM nginx:latest

COPY nginx.conf /etc/nginx/nginx.conf
COPY ledger-board.conf /etc/nginx/sites-available/ledger-board.conf

RUN mkdir /etc/nginx/sites-enabled
RUN ln -s /etc/nginx/sites-available/ /etc/nginx/sites-enabled/

EXPOSE 80 80
