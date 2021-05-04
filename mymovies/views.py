from django.http import HttpResponse ,JsonResponse
from django.shortcuts import render
import requests
from requests.auth import HTTPBasicAuth
import json
from django.template import loader
from . models import Movie

user_name = 'iNd3jDMYRKsN1pjQPMRz2nrq7N99q4Tsp9EY9cM0'
password = 'Ne5DoTQt7p8qrgkPdtenTK8zd6MorcCR5vXZIJNfJwvfafZfcOs4reyasVYddTyXCz9hcL5FGGIVxw3q02ibnBLhblivqQTp4BIC93LZHj4OppuHQUzwugcYu7TIC5H1'


def movies(request):
	response = requests.get(
		'https://demo.credy.in/api/v1/maya/movies/',
		auth = HTTPBasicAuth(user_name, password) 
		)
	movies = response.json()
	for x in movies['results']:
		m = Movie(title = x['title'], uuid = x['uuid'], description = x['description'] , genres = x['genres'] )
		m.save()
	return JsonResponse(movies)


def register(request):
	return HttpResponse("You are at the register page")

