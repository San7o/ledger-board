import {Component} from '@angular/core';
import { ReactiveFormsModule, FormControl, FormGroup } from '@angular/forms'
import { RouterLink } from '@angular/router';

/*
 *  {
 *      date: "YYYY/MM/DD",
 *      payee: "Name of the payee",
 *      amount: "100.00",
 *      currency: "EUR",
 *      expenses_account: "Expenses:Account",
 *      assets_account: "Assets:Account"
 *  }
 */

@Component({
  selector: 'app-root',
  template: `

    <h1>Record your transaction</h1>

    <form [formGroup]="sendForm"
          (ngSubmit)="handleSubmit()">

      <label>
        Date
        <input type="date" formControlName="date" required/>
      </label><br>

      <label>
        Payee
        <input type="text" formControlName="payee" required/>
      </label><br>

      <label>
        Amount 
        <input type="number" formControlName="amount" required/>
      </label><br>

      <label>
        Currency
        <input type="text" formControlName="currency" required/>
      </label><br>

      <label>
        Expenses Account
        <input type="text" formControlName="expenses_account" required/>
      </label><br>

      <label>
        Assets Account
        <input type="text" formControlName="assets_account" required/>
      </label><br>

      <button type="submit">Submit</button>

    </form>
    <p>{{ info_message }}</p><br>

    <a routerLink="/">Torna alla Home</a>
  `,
  standalone: true,
  imports: [ReactiveFormsModule, RouterLink],
})
export class SendComponent {

  info_message = '';

  sendForm = new FormGroup({
    date: new FormControl(''),
    payee: new FormControl(''),
    amount: new FormControl(''),
    currency: new FormControl(''),
    expenses_account: new FormControl(''),
    assets_account: new FormControl(''),
  });


  handleSubmit() {


    // Ceck that all the fields are filled
    if (
      this.sendForm.value.date === '' ||
      this.sendForm.value.payee === '' ||
      this.sendForm.value.amount === '' ||
      this.sendForm.value.currency === '' ||
      this.sendForm.value.expenses_account === '' ||
      this.sendForm.value.assets_account === ''
    ) {
      this.info_message = 'Please fill all the fields';
      return;
    }

    // Change date format to YYYY/MM/DD
    this.sendForm.value.date = this.sendForm.value.date!.split('-').join('/');
    
    fetch('http://localhost:8000/api/sender/send', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(this.sendForm.value),
        })
        .then((response) => response.json())
        .then((data) => {
          console.log('Success:', data);
          this.info_message = 'Transaction recorded';
        })
        .catch((error) => {
          console.error('Error:', error);
          this.info_message = 'Error recording transaction';
        });
    
  }


}
