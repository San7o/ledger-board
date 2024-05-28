# ledger-board

## Project Goals

I am creating this application as a practice project to learn more about
- big data
- neural networks
- web frameworks

## Project Statement

This project aims to build a web app visualizer for personal finance data, saved in [Ledger](https://github.com/ledger/ledger) format. The application will use **neural networks** to predict the next transactions. 

The application will use the following technologies:
- [x] `backend`: Django
- [x] `frontend`: Angular
- [x] `Gunicorn`: performant WSGI
- [x] `Nginx`:
    - [x] Cache
    - [x] Static content server for frontend
    - [x] Proxy
- [ ] `database`: Redis
- [ ] `big data management`: Spark, kafka,
- [ ] `structured logging`: sentry, jsonlogs
- [ ] `linter`
- [ ] `unit tests`
- [ ] full `github` workflow with issues, roadmap and milestones

Deploy / Infrastructure
- [x] Containerized with docker
- [x] Production infrastructure
- [ ] Deploy with [kubernetes](https://github.com/kubernetes/kubernetes)
- [ ] Managing with Terraform

## Developement

We strongly encourage to use Nix to have a consistant developement environment across devices. You can enter the developement environmenti with the following command:
```bash
nix develop
```

If you don't have nix, you nee to have `python3` and you need to install all the dependencies.
You can use a virtual environment to download dependencies, you can place the environment to `backend/` folder bit It's up to what your preference.
```bash
python3 -m venv backend/
```
You can install dependencies via pip:
```bash
pip install -r requirements.txt
```

### Running the project

You can run the backend in developement server with the following command inside `backend/`:
```bash
python3 manage.py runserver 
```
For production, use gunicorn:
```bash
gunicorn -c gunicorn.conf.py backend.wsgi
```

You can run the frontend with the following command, after you have installed necessary modules via `npm i`:
```bash
cd frontend
npx ng serve --open
```
Or you can build for production with:
```build
npx ng build --configuration=production
```

## Develop with docker

Docker is very handy to setup our dev environment. You can build the docker network with:
```bash
sudo docker build .
```
Run the containers with docker compose:
```bash
sudo docker compose up --build
```
This will create 3 images:
- `frontend` image, runnin in `$LEDGER_BOARD_FRONTEND:4200`
- `backend` image, running in `$LEDGER_BOARD_BACKEND:8000`
- `nginx` image, running in `$LEDGER_BOARD_BACKEND:80`

You should use the nginx server to test the application. It's also the only one connected to the host network when running in production.

The environment values are located in `.env`

Those containers use volumes, so that they don't copy any data inside: both frontend and backend automatically restart after you make a change in the code. This is very handy but avaiavle only for developement, we need a different infrastructure for production. 

# Run in Production

For production we can't use shared volumes (kubernetes doesn't let us and It's not a good choice), to run the infrastructure for production with docker, run:
```bash
sudo docker compose -f docker-compose.production.yaml up --build
```
There are different dockeer configs for production for each container, those contain the string `.production` in the name
