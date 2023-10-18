from django.shortcuts import render
from django.views import View

from movies.models import Movie


class MoviesView(View) :

    def get(self, request) :
        movies = Movie.objects.all()
        return render(request, 'movies/movies.html', {'movies_list' : movies})
