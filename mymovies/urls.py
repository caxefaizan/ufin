from django.urls import path
from . import views 
urlpatterns = [
    path('movies/', views.movies, name = 'movies'),
    path('Register/', views.register, name = 'register'),
]
