from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import View
from math import factorial
import json
import requests

# Create your views here.
@csrf_exempt
@require_http_methods(['GET', 'POST'])
def factorial_func(request):
    if request.method == 'GET':
        number = int(request.GET.get('number'))  #http://127.0.0.1:8000/hm21_volkau/factorial?number=any number вводим число для определения факториала#
        if number <= 0:
            factorial_num = None
            message = "Plesae enter a valid number"
        elif number == 1:
            factorial_num = 1
            message = "Successful operation"
        else:
            message = "Successful operation"
            factorial_num = factorial(number)

        data = {
            'original_input': number,
            'message': message,
            'result': factorial_num
        }
        return JsonResponse(data)
    elif request.method == 'POST':
        return HttpResponse("For calculating the factorial of a number, use the GET method")

class KanyeWestView(View):
    message = 'Kanye West is God!!!!!'
    def get(self, request, *args, **kwargs):

        if kwargs.get('quotes'):
            quotnumber = kwargs['quotes']
            quotnumber = int(quotnumber)
        else:
            quotnumber = 1
        kanye_quotes = [requests.get('https://api.kanye.rest').json()['quote'] for x in range(quotnumber)]
        return render(request, 'hm21_volkau/kanyewestquotes.html', {'list': kanye_quotes})