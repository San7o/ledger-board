"""The module contains the view that will send the transaction data to the server."""
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from sender.utils.checks import check_fields, check_currency, check_date, check_amount
from celeryApp.SenderClass import SenderClass
import json
import logging

# Create a logger object
logger = logging.getLogger('django')

@csrf_exempt
async def send_data(request):
    """Send data API endpoint.
       Method: POST

       Given the trnsaction data, this view will send it to the server.
       The data must be sent in teh body and must follow the following json format:

       {
           date: "YYYY/MM/DD",
           payee: "Name of the payee",
           amount: "100.00",
           currency: "EUR",
           expenses_account: "Expenses:Account",
           assets_account: "Assets:Account"
        }
        
        Description:
        - date: The date of the transaction.
        - payee: The name of the payee.
        - amount: The amount of the transaction.
        - currency: The currency of the transaction.
        - expenses_account: The account where the expenses will be recorded.
        - assets_account: The account where the amount will be prelevated.

    """
    if request.method == "POST":
        try:
            data = json.loads(request.body)

            # Check if the data is in the correct format
            if not check_fields(data):
                return JsonResponse({"message": "Invalid JSON format."},
                                    status=400)

            if not check_currency(data["currency"]):
                return JsonResponse({"message": "Invalid currency."},
                                    status=400)

            if not check_date(data["date"]):
                return JsonResponse({"message": "Invalid date format."},
                                    status=400)
           
            if not check_amount(data["amount"]):
                return JsonResponse({"message": "Invalid amount."},
                                    status=400)

            # Call the celery task to send the data asynchronously
            if not SenderClass.send.delay("transactions", json.dumps(data)):
                return JsonResponse({"message": "Error sending data."},
                                    status=500)

            # OK
            return JsonResponse({"message": "Data sent successfully."},
                                status=200)

        except json.JSONDecodeError:

            return JsonResponse({"message": "Invalid JSON format."},
                                status=400)

    return JsonResponse({"message": "Invalid request method."},
                        status=405)
