import { bootstrapApplication } from '@angular/platform-browser';
import { appConfig } from './app/config/config';
import { AppComponent } from './app/components/appComponent';

bootstrapApplication(AppComponent, appConfig)
  .catch((err) => console.error(err));
