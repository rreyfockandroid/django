from django.http import HttpResponse
from datetime import datetime

def helloX(request):
   text = "<h1>Witaj w mojej aplikacji!</h1>"
   return HttpResponse(text)

def morning(request):
	text = "Good morning"
	return HttpResponse(text)

def viewArticle(request, articleId):
	text = "Wyswietl artykul numer: %s"%articleId
	return HttpResponse(text)

def viewArticles(request, month, year):
	text = "Wyswietl artykul z: %s/%s"%(year, month)
	return HttpResponse(text)

from django.shortcuts import render

def hello(request):
	today = datetime.now().date()
	infotext = 'nazywam sie alicja'
	return render(request, "hello.html", {"today":today, "infotext":infotext})
