from django.shortcuts import render
from django.views import View
from django.views.generic import ListView, DetailView

from movies.models import Movie


class MoviesView(ListView) :
    model = Movie
    queryset = Movie.objects.filter(draft=False)
    context_object_name = 'movies'


class MovieDetailView(DetailView) :
    model = Movie
    slug_field = 'url'
