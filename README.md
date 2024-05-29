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
- [x] `backend ASGI`: Uvicorn
- [x] `frontend`: Angular
- [x] `Nginx`:
    - [x] Cache
    - [x] Static content server for frontend
    - [x] Proxy
- [x] `database`: Redis
- [x] `structured logging`: jsonlogs
- [ ] `linter`
- [ ] `unit tests`
- [ ] `big data management`: Spark, kafka,
- [ ] full `github` workflow with issues, roadmap and milestones

Deploy / Infrastructure
- [x] Containerized with docker
- [x] Production infrastructure
- [x] Deploy with [kubernetes](https://github.com/kubernetes/kubernetes)

## Developement

We strongly encourage to use Nix to have a consistant developement environment across devices.

You can enter the developement environmenti with the following command:
```bash
nix develop
```

If you don't have nix, you need to have `python3` and `node 20` and to install all the dependencies.

You can use a virtual environment to download dependencies, you can place the environment to `backend/` folder but It's up to your preference.
```bash
python3 -m venv backend/
```
You can install dependencies for python via pip:
```bash
cd backend && pip install -r requirements.txt
```
Yon can install delendencies for Node via npm
```bash
cd forntend && npm i
```

### Running the project

You can run the backend in developement server with the following command inside `backend/`:
```bash
python3 manage.py runserver 
```
For production, use gunicorn + uvicorn:
```bash
gunicorn -c gunicorn.conf.py backend.asgi -k uvicorn.worker.UvicornWorker
```

You can run the frontend in dev mode with the following command:
```bash
cd frontend
npx ng serve --open
```
Or build for production with:
```build
npx ng build --configuration=production
```
You also need docker to run nginx and for production


## Develop with docker

First, make sure you have the correct npm modules installed:
```bash
cd frontend && npm i
```

Docker is very handy to setup our dev environment. 

Run the containers with docker compose:
```bash
sudo docker compose up --build
```
This will create and run 4 containers:
- `frontend` image, runnin in `$LEDGER_BOARD_FRONTEND:4200`
- `backend` image, running in `$LEDGER_BOARD_BACKEND:8000`
- `nginx` image, running in `$LEDGER_BOARD_NGINX:80`
- `redit` image, running in `$LEDGER_BOARD_REDIS:6379`

You should use the nginx server to test the application. It's also the only one connected to the host network when running in production.

The environment values are located in `.env`

Those containers use volumes, so that they don't copy any data inside: both frontend and backend automatically restart after you make a change in the code. This is very handy but available only for developement, we need a different infrastructure for production. 

# Run in Production

First, mae sure you have build the frontend for production:
```bash
cd frontend && npm i
npx ng build --configuration=production
```

For production we can't use shared volumes (kubernetes doesn't let us and It's not a good choice), to run the infrastructure for production with docker, run:
```bash
sudo docker compose -f docker-compose.production.yaml up --build
```
There are different docker configs for production for each container, those contain the string `.production` in the name.
- the backend uses gunicorn
- the frontend uses nginx to serve static files
- nginx is used as cache and proxy. The cache is only effective when running in production.

## Deploy with kubernetes

You need `kind` installed for local test deploy. First, create a cluster with the following command:
```bash
cd kubernetes &&
sudo kind create cluster --name ledger-board-cluster --config kubernetes-config.yaml
```
Then load the docker images:
```bash
sudo kind load docker-image ledger-board-nginx --name ledger-board-cluster
sudo kind load docker-image ledger-board-backend --name ledger-board-cluster
sudo kind load docker-image ledger-board-backend --name ledger-board-cluster
```
In actual procuction, you would have to publish the images in some repo. This also enables easy CD.

Load the pod and a service with:
```bash
sudo kubectl apply -f ledger-board-nginx-service.yaml
sudo kubectl apply -f ledger-board-pod.yaml
```
Check pod status:
```bash
sudo kubectl get pods
```
Test by connecting to nginx:
```bash
sudo kubectl port-forward ledger-board-application 80:80
```

More verbose explaination can be found in `kubernetes/README.md`

Note: We are not using a database inside the local cluster, since It's much more stable to use a well known distributed DB provider. The connection to the DB shall be made to the provider. So far, I didn't set up any online instance so the kubernetes cluster won't be able to connect to the DB.
