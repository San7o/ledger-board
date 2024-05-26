import { Component } from '@angular/core';
import { RouterLink, RouterOutlet } from '@angular/router';

@Component({
  selector: 'app-root',
  standalone: true,
  imports: [RouterLink, RouterOutlet],
  template: `
        <p>Welcome to the Homepage!</p>
        <router-outlet />
        <a routerLink="/greet">Greet</a>
  `,
  // styleUrl: './app.component.scss'
})
export class HomeComponent {
  title = 'frontend';
}
