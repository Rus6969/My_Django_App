from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
# from django.template.loader import render_to_string
# Create your views here.

monthly_challenges = {"january": "NO meat in Jan",
                      "february": "zero carbs in feb ",
                      "march": "no shave march"}


def monthly_challenge_byNumber(request, month):
    months = list(monthly_challenges.keys())

    redirect_month = months[month-1]

    redirect_path = reverse(
        "month-challenge", args=[redirect_month])  # /challenge

    return HttpResponseRedirect(redirect_path)


def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month]

        #response_data = render_to_string("challenges/challenge.html")
        return render(request,"challenges/challenge.html",{"text":challenge_text,
                                                           "month_name":month.capitalize()
                                                           })

    except:
        return HttpResponseNotFound("no Such month supported ")
    
