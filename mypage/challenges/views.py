from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
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

    except:
        return HttpResponseNotFound("no Such month supported ")
    return HttpResponse(challenge_text)
