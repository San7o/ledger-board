# Frontend

This project was generated with [Angular CLI](https://github.com/angular/angular-cli) version 18.0.1.

## Development server

Run `ng serve` for a dev server. Navigate to `http://localhost:4200/`. The application will automatically reload if you change any of the source files.

## Code scaffolding

Run `ng generate component component-name` to generate a new component. You can also use `ng generate directive|pipe|service|class|guard|interface|enum|module`.

## Build

Run `ng build` to build the project. The build artifacts will be stored in the `dist/` directory.

## Lint

To use eslint, run
```bash
npx ng lint
```

## Deploy with docker

You can deploy the frontend for production via Nginx in a docker image. Run the following commands:
```bash
sudo docker build -t frontend-nginx --file Dockerfile.production .
sudo docker run --net host frontend-nginx
```

## Running unit tests

Run `ng test` to execute the unit tests via [Karma](https://karma-runner.github.io).

## Running end-to-end tests

Run `ng e2e` to execute the end-to-end tests via a platform of your choice. To use this command, you need to first add a package that implements end-to-end testing capabilities.

## Tailwind

The frontend uses tilewindcss as a css framework. It was set up following [this](https://tailwindcss.com/docs/guides/angular) guide.

## Further help

To get more help on the Angular CLI use `ng help` or go check out the [Angular CLI Overview and Command Reference](https://angular.dev/tools/cli) page.
