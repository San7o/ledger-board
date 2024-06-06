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

  <!-- sample form
    <h1 class="text-3xl font-bold underline" >Record your transaction</h1>

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

   -->


<!-- form with tailwindcss https://v1.tailwindcss.com/components/forms -->

<!-- centre the form -->
<div class="flex items-center justify-center min-h-screen">


<form
    [formGroup]="sendForm"
    (ngSubmit)="handleSubmit()"
    class="w-full max-w-lg"
>


  <p
     class="block uppercase tracking-wide text-gray-700 text-3xl font-bold mb-2" >
        Record your transaction
  </p><br>

  <!-- two elements -->
  <div class="flex flex-wrap -mx-3 mb-6">

  <!-- date -->
    <div class="w-full md:w-1/2 px-3 mb-6 md:mb-0">
      <label class="block uppercase tracking-wide text-gray-700 text-xs font-bold mb-2" for="date">
      Date
      </label>
      <input
        class="appearance-none block w-full bg-gray-200 text-gray-700 border  rounded py-3 px-4 mb-3 leading-tight focus:outline-none focus:bg-white"
        formControlName="date"
        type="date"
        required
      >
    </div>

    <!-- payee -->
    <div class="w-full md:w-1/2 px-3">
      <label class="block uppercase tracking-wide text-gray-700 text-xs font-bold mb-2" for="payee">
        Payee
      </label>
      <input class="appearance-none block w-full bg-gray-200 text-gray-700 border border-gray-200 rounded py-3 px-4 leading-tight focus:outline-none focus:bg-white focus:border-gray-500" formControlName="payee" type="text" placeholder="McDonald" required>
    </div>
  </div>


  <!-- two elements -->
  <div class="flex flex-wrap -mx-3 mb-2">

    <!-- amount -->
    <div class="w-full md:w-1/2 px-3 mb-6 md:mb-0">
      <label class="block uppercase tracking-wide text-gray-700 text-xs font-bold mb-2" for="grid-city">
        Amount
      </label>
      <input class="appearance-none block w-full bg-gray-200 text-gray-700 border border-gray-200 rounded py-3 px-4 leading-tight focus:outline-none focus:bg-white focus:border-gray-500" formControlName="amount" type="text" placeholder="100.00">
    </div>
    
    <!-- currency -->
    <div class="w-full md:w-1/2 px-3 mb-6 md:mb-0">
      <label class="block uppercase tracking-wide text-gray-700 text-xs font-bold mb-2" for="grid-state">
        Currency
      </label>
      <div class="relative">
        <select class="block appearance-none w-full bg-gray-200 border border-gray-200 text-gray-700 py-3 px-4 pr-8 rounded leading-tight focus:outline-none focus:bg-white focus:border-gray-500" formControlName="currency">

    <!--

    USD = "$"         # United States Dollar
    EUR = "€"         # Euro
    GBP = "£"         # British Pound
    JPY = "¥"         # Japanese Yen
    CHF = "CHF"       # Swiss Franc
    CAD = "CAD"       # Canadian Dollar
    AUD = "AUD"       # Australian Dollar

    -->
          <option>$</option>
          <option>€</option>
          <option>£</option>
          <option>¥</option>
          <option>CHF</option>
          <option>CAD</option>
          <option>AUD</option>
          <option>Other</option>
        </select>
        <div class="pointer-events-none absolute inset-y-0 right-0 flex items-center px-2 text-gray-700">
          <svg class="fill-current h-4 w-4" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 20 20"><path d="M9.293 12.95l.707.707L15.657 8l-1.414-1.414L10 10.828 5.757 6.586 4.343 8z"/></svg>
        </div>
      </div>
    </div>
  </div>


  <!-- assets account -->
  <div class="flex flex-wrap -mx-3 mb-6">
    <div class="w-full px-3">
      <label class="block uppercase tracking-wide text-gray-700 text-xs font-bold mb-2" for="assets_account">
        Assets Account
      </label>
      <input class="appearance-none block w-full bg-gray-200 text-gray-700 border border-gray-200 rounded py-3 px-4 mb-3 leading-tight focus:outline-none focus:bg-white focus:border-gray-500" formControlName="assets_account" type="text" placeholder="">
      <p class="text-gray-600 text-xs italic">From where you are withdrawing money</p>
    </div>
  </div>


  <!-- expenses account -->
  <div class="flex flex-wrap -mx-3 mb-6">
    <div class="w-full px-3">
      <label class="block uppercase tracking-wide text-gray-700 text-xs font-bold mb-2" for="assets_account">
        Expenses Account
      </label>
      <input class="appearance-none block w-full bg-gray-200 text-gray-700 border border-gray-200 rounded py-3 px-4 mb-3 leading-tight focus:outline-none focus:bg-white focus:border-gray-500" formControlName="expenses_account" type="text" placeholder="">
      <p class="text-gray-600 text-xs italic">Where is the transaction going</p>
    </div>
  </div>


  <!-- submit button -->
  <div class="flex flex-wrap -mx-3 mb-6">
    <div class="w-full px-3">
      <button class="block uppercase tracking-wide text-gray-700 text-xs font-bold mb-2 text-blue-500 hover:text-blue-800" type="submit">
        Submit</button>
    </div>
  </div>
      
  <p class="text-red-500 text-xs italic">{{ info_message }}</p><br>

    <!-- home button -->
    <a class="block uppercase tracking-wide text-gray-700 hover:text-blue-800  text-xl font-bold mb-2" routerLink="/">Torna alla Home</a>

</form>


</div>


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
