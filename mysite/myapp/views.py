from django.http import HttpResponse
from datetime import datetime
import django
import platform

def helloX(request):
    dver = django.get_version()
    pver = platform.python_version()
    text = "<h1>Witaj w mojej aplikacji! Version, python: %s, django: %s</h1>"% (pver, dver)
    return HttpResponse(text)


def morning(request):
    text = "Good morning"
    return HttpResponse(text)


def viewArticle(request, articleId):
    text = "Wyswietl artykul numer: %s" % articleId
    return HttpResponse(text)


def viewArticles(request, month, year):
    text = "Wyswietl artykul z: %s/%s" % (year, month)
    return HttpResponse(text)


from django.shortcuts import render


def hello(request):
    today = datetime.now().date()
    infotext = 'nazywam sie alicja'
    return render(request, "hello.html", {"today": today, "infotext": infotext})
