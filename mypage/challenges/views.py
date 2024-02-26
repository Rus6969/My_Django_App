from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
# Create your views here.


def index(request):
    return HttpResponse("This works")


def february(request):
    return HttpResponse("Februrary works")


def monthly_challenge(request,month):
    challenge_text = None
    if month == 'january':
        challenge_text = "no meat in January"
    elif month =='february':
        challenge_text = "no shave February"    
    else:
        return  HttpResponseNotFound ( "no Such month supported ")
        
    return HttpResponse(challenge_text)