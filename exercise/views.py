from django.shortcuts import render
import requests


def home(request):
    response_words = requests.get('https://run.mocky.io/v3/92f3a2e6-1686-454b-9847-5e625bc5959f')
    words = response_words.json()

    response_phrases = requests.get('https://run.mocky.io/v3/4d176167-1c9c-45af-a74e-679f949cbd0e')
    phrases = response_phrases.json()

    return render(request, 'home.html', {'words': words, 'phrases': phrases})
