# ledger-board

## Project Goals

I am creating this application as a practice project to learn more about
- big data
- neural networks
- web frameworks

## Project Statement

This project aims to build a web app visualizer for personal finance data, saved in [Ledger](https://github.com/ledger/ledger) format. The application will use **neural networks** to predict the next transactions. The application will use the following technologies:
- [x] backend: python (Django)
- [x] frontend: Angular
- [x] Gunicorn for serving WSGI server
- [x] Nginx as load manager and proxy
- [ ] database: Redis
- [ ] big data management: Spark, kafka,
- [ ] structured logging: sentry, jsonlogs
- [ ] some kind of linter
- [ ] unit tests
- [ ] fully github workflow with issues, roadmap and milestones
- [ ] Nginx to manage apis

Deploy / Infrastructure
- [x] Containerized with docker
- [ ] deploy with [kubernetes](https://github.com/kubernetes/kubernetes)
- [ ] managing with Terraform

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

You can run the backend in developement mode with the following command inside `backend/`:
```bash
python3 manage.py runserver 
```
For deployment, use gunicorn:
```bash
gunicorn -c gunicorn.conf.py backend.wsgi
```

You can run the frontend with the following command, after you have installed necessary modules via `npm i`:
```bash
cd frontend
npx ng serve --open
```

## Build the application
Build the docker image:
```bash
sudo docker build .
```
Run the image with docker compose:
```bash
sudo docker compose up --build
```
This will create 3 images:
- `frontend` image, accessible via `$LEDGER_BOARD_FRONTEND:4200`
- `backend` image, accessible via `$LEDGER_BOARD_BACKEND:8000`
- `nginx` image, accessible via `$LEDGER_BOARD_BACKEND:80`
The environment values are located in `.env`
