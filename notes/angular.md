# Angular

## base logic

If statements:
```javascript
@Component({
  ...
  template: `
    @if (isLoggedIn) {
      <p>Welcome back, Friend!</p>
    }
  `,
})
class AppComponent {
  isLoggedIn = true;
}
```

For loops:
```javascript
@Component({
  ...
  template: `
    @for (os of operatingSystems; track os.id) {
      {{ os.name }}
    }
  `,
})
export class AppComponent {
  operatingSystems = [{id: 'win', name: 'Windows'}, {id: 'osx', name: 'MacOS'}, {id: 'linux', name: 'Linux'}];
}
```

Set html attributes to the component variables:
```javascript
@Component({
  selector: 'app-root',
  styleUrls: ['app.component.css'],
  template: `
    <div [contentEditable]="isEditable"></div>
  `,
  standalone: true,
})
export class AppComponent {
  isEditable = false;
}
```

Event handling
```javascript 
@Component({
    ...
    template: `<button (click)="greet()">`
})
class AppComponent {
    greet() {
        console.log('Hello, there 👋');
    }
}
```
Call functions:
```javascript
@Component({
  selector: 'app-root',
  template: `
    <section (mouseover)="onMouseOver()">
      There's a secret message for you, hover to reveal 👀
      {{ message }}
    </section>
  `,
  standalone: true,
})
export class AppComponent {
  message = '';

  onMouseOver() {
    this.message = "less go";
  }
}
```

## multi-component communication
Pass parameters to components:
`Component A`
```javascript
import {Component, Input} from '@angular/core';

@Component({
  selector: 'app-user',
  template: `
    <p>The user's name is {{occupation}}</p>
  `,
  standalone: true,
})
export class UserComponent {
  @Input() occupation = ''; // Notice here
}
```
`Component B`
```javascript
import {Component} from '@angular/core';
import {UserComponent} from './user.component';

@Component({
  selector: 'app-root',
  template: `
    <app-user occupation="Simiran" />
  `,
  standalone: true,
  imports: [UserComponent],
})
export class AppComponent {}
```

Ouput()
`Emitter Component`
```javascript
@Component({
  selector: 'app-child',
  styles: `.btn { padding: 5px; }`,
  template: `
    <button class="btn" (click)="addItem()">Add Item</button>
  `,
  standalone: true,
})
export class ChildComponent {
  @Output() addItemEvent = new EventEmitter<string>();
  
  addItem() {
    this.addItemEvent.emit('nuovo');
  }
}
```
`Receiver Component`
```javascript
@Component({
  selector: 'app-root',
  template: `
    <app-child (addItemEvent)='addItem($event)' />
    <p>🐢 all the way down {{ items.length }}</p>
  `,
  standalone: true,
  imports: [ChildComponent],
})
export class AppComponent {
  items = new Array();

  addItem(item: string) {
    this.items.push(item);
  }
}
```
## optimization: defer

Defer: load on an event. `on viewport` means when the content is viewed
```javascript
    @defer (on viewport) { 
      <comments />
    } @placeholder {
      <p>FUTURE COMMENTS</p>
    } @loading (minimum 2s) {
      <p>Loading...</p>
    }
```

## load images best practices
loading images may be a bottleneck on performance, here are some best practices
```javascript
import {Component} from '@angular/core';
import { NgOptimizedImage, provideImgixLoader } from '@angular/common';

@Component({
  standalone: true,
  selector: 'app-user',
  template: `
    <p>Username: {{ username }}</p>
    <p>Preferred Framework:</p>
    <ul>
      <li>
        Static Image:

        <!-- priority -->
        <img ngSrc="/assets/logo.svg" alt="Angular logo" priority/> 
      </li>
      <li>
        Dynamic Image:
        <div class"image-container" style="porision: fill">
          <img [ngSrc]="logoUrl" [alt]="logoAlt" fill />
        </div>
      </li>
    </ul>
  `,
  imports: [NgOptimizedImage],
  providers: [
    // To use image CDN
    provideImgixLoader('https://my.base.url'),
  ]
})
export class UserComponent {
  logoUrl = '/assets/logo.svg';
  logoAlt = 'Angular logo';
  username = 'youngTech';
}
```
- use `NgOptimizedImage` and put ngSrc tags
- add priority tags
- use fill instead of height and width
- use image CDN

## routing



Add routes
`app.routes.ts`
```javascript
import {Routes} from '@angular/router';
import {HomeComponent} from './home/home.component';
import {UserComponent} from './user/user.component';

export const routes: Routes = [
  {
    path: '',
    title: 'App Home Page',
    component: HomeComponent,
  },
];
```
`app.config.ts`
```javascript
import {ApplicationConfig} from '@angular/core';
import {provideRouter} from '@angular/router';
import {routes} from './app.routes';
export const appConfig: ApplicationConfig = {
  providers: [provideRouter(routes)],
};
```
Add router outlet `<router-outlet />` where you want to render the route content's. Use routerLink to not refresh the page
```javascript
import {Component} from '@angular/core';
import {RouterOutlet, RouterLink} from '@angular/router';

@Component({
  selector: 'app-root',
  template: `
    <nav>
      <a routerLink="/">Home</a>
      |
      <a routerLink="/user">User</a>
    </nav>
    <router-outlet />
  `,
  standalone: true,
  imports: [RouterOutlet, RouterLink],
})
export class AppComponent {}
```

## forms

In Angular, there are two types of forms: template-driven and reactive.

### Template driven:
```javascript
import {Component} from '@angular/core';
import {FormsModule} from '@angular/forms'

@Component({
  selector: 'app-user',
  template: `
    <p>Username: {{ username }}</p>
    <p>{{ username }}'s favorite framework: {{ favoriteFramework }}</p>
    <label for="framework">
      Favorite Framework:
      <input id="framework" type="text" [(ngModel)]="favoriteFramework" />
    </label>
  `,
  standalone: true,
  imports: [FormsModule],
})
export class UserComponent {
  username = 'youngTech';
  favoriteFramework = '';
}
```
Note: The syntax [()] is known as "banana in a box" but it represents two-way binding: property binding and event binding. 
call function:
```javascript
import {Component} from '@angular/core';
import {FormsModule} from '@angular/forms';

@Component({
  selector: 'app-user',
  template: `
    <p>Username: {{ username }}</p>
    <p>Framework: {{favoriteFramework}}</p>
    <label for="framework">
      Favorite Framework:
      <input id="framework" type="text" [(ngModel)]="favoriteFramework" />
    </label>
    <button (click)="showFramework()">Show Framework</button>
  `,
  standalone: true,
  imports: [FormsModule],
})
export class UserComponent {
  favoriteFramework = '';
  username = 'youngTech';

  showFramework() {
    alert(this.favoriteFramework)
  }
}
```
### Reactive forms
Mi piace di più
```javascript
import {Component} from '@angular/core';
import { ReactiveFormsModule, FormControl, FormGroup } from '@angular/forms'

@Component({
  selector: 'app-root',
  template: `
    <form [formGroup]="profileForm"
          (ngSubmit)="handleSubmit()">
      <label>
        Name
        <input type="text" formControlName="name" />
      </label>
      <label>
        Email
        <input type="email" formControlName="email" />
      </label>
      <button type="submit">Submit</button>
    </form>
  `,
  standalone: true,
  imports: [ReactiveFormsModule],
})
export class AppComponent {

  profileForm = new FormGroup({
    name: new FormControl(''),
    email: new FormControl(''),
  });

        
  handleSubmit() {
    alert(
      this.profileForm.value.name + ' | ' + this.profileForm.value.email
    );
  }

    
}
```

### Validators
Validate a form
This example disables the sumbit button if the requirements are not met. The requirements are defined in the FormGroup()
```javascript
import {Component} from '@angular/core';
import {FormGroup, FormControl} from '@angular/forms';
import {ReactiveFormsModule, Validators } from '@angular/forms';

@Component({
  selector: 'app-root',
  template: `
    <form [formGroup]="profileForm">
      <input type="text" formControlName="name" name="name" />
      <input type="email" formControlName="email" name="email" />
      <button type="submit" [disabled]="!profileForm.valid">Submit</button>
    </form>
  `,
  standalone: true,
  imports: [ReactiveFormsModule],
})
export class AppComponent {
  profileForm = new FormGroup({
    name: new FormControl('', Validators.required),
    email: new FormControl('', [Validators.required, Validators.email]),
  });
}
```

## Dependency Injection
We use the decorator `@Injectable` and the scope
```javascript
import {Injectable} from '@angular/core';

@Injectable({
  providedIn: `root`
})
export class CarService {
  cars = ['Sunflower GT', 'Flexus Sport', 'Sprout Mach One'];

  getCars(): string[] {
    return this.cars;
  }

  getCar(id: number) {
    return this.cars[id];
  }
}
```
Read the injection
- load the variable with the `inject()` function
```javascript
import {Component, inject} from '@angular/core';
import {CarService} from './car.service';

@Component({
  selector: 'app-root',
  template: `
    <p>Car listing: {{ display }}</p>
  `,
  standalone: true,
})
export class AppComponent {
  display = '';

  carService = inject(CarService);
  
  constructor() {
    this.display = this.carService.getCars().join(' ');
  }
}
```

## Pipes

You can pipe data into pipes, like linux pipes! for example piping a string into a lowercase function.
```javascript
import {Component} from '@angular/core';
import { LowerCasePipe } from '@angular/common'

@Component({
  selector: 'app-root',
  template: `
    {{ username | lowercase }}
  `,
  standalone: true,
  imports: [LowerCasePipe],
})
export class AppComponent {
  username = 'yOunGTECh';
}
```

You can format date or time or any string into any format.

### Create your own pipe
Add `@Pipe` decorator and define the function
`reverse.pipe.ts`
```javscript
import {Pipe, PipeTransform} from '@angular/core';

@Pipe({
  standalone: true,
  name: 'reverse',
})
export class ReversePipe implements PipeTransform {
  transform(value: string): string {
    let reverse = '';

    for (let i = value.length -1; i >= 0; i--) {
      reverse += value[i];
    }
    return reverse;
  }
}
```
Use it
```javascript
import {Component} from '@angular/core';
import {ReversePipe} from './reverse.pipe';

@Component({
  selector: 'app-root',
  template: `
    Reverse Machine: {{ word | reverse }}
  `,
  standalone: true,
  imports: [ReversePipe],
})
export class AppComponent {
  word = 'You are a champion';
}
```
