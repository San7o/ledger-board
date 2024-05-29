import { Component } from '@angular/core';
import { RouterLink } from '@angular/router';
import { HttpClient, HttpClientModule } from '@angular/common/http';

@Component({
  selector: 'app-root',
  standalone: true,
  imports: [RouterLink, HttpClientModule],
  template: `
        <button (click)="callApi()">Call API</button>
        <p>Messaggio: {{ message }}</p>
        <a routerLink="/">Torna alla Home</a>
  `,
  // styleUrl: './app.component.scss'
})
export class GreetComponent {

    message = '';

    constructor(private http: HttpClient) { }

    // Make request to backend
    callApi(): void {
        this.http.get<JSON>("/api/greet").subscribe((data: JSON) => {
            this.message = JSON.stringify(data);
            console.log(data);
        },
        (error) => console.log(error)
        );

    }

}
