from django.db.models import Q
from django.views.generic import ListView, DetailView

from movies.models import Movie, Genre


class GenreYear():
    def get_genres(self):
        return Genre.objects.all()

    def get_years(self):
        return Movie.objects.filter(draft=False).values('year')


class MoviesView(ListView, GenreYear) :
    model = Movie
    queryset = Movie.objects.filter(draft=False)
    context_object_name = 'movies'


class MovieDetailView(DetailView, GenreYear) :
    model = Movie
    slug_field = 'url'


class FilterMoviesView(ListView, GenreYear):
    context_object_name = 'movies'

    def get_queryset(self):
        queryset = Movie.objects.filter(
            Q(year__in=self.request.GET.getlist('year')) |
            Q(genres__in=self.request.GET.getlist('genre'))
        )
        return queryset
