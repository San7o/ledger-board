/*
 *   This file is used to define the routes of the application.
 */ 
import { Routes } from '@angular/router';
import { GreetComponent } from '../components/greetComponent';
import { HomeComponent } from '../components/homeComponent';

export const routes: Routes = [
    {
        path: '',
        title: 'Home',
        component: HomeComponent,
    },
    {
        path: 'greet',
        title: 'Greet',
        component: GreetComponent,
    },
];
