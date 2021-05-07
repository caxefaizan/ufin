from django.urls import path
from . import views 
from . api import RegisterApi


urlpatterns = [
    path('movies/', views.movies, name = 'movies'),
    path('register/', RegisterApi.as_view()),
]
