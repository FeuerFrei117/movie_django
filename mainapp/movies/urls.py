from django.urls import path

from movies.views import MoviesView, MovieDetailView

app_name = 'movies'

urlpatterns = [
    path('', MoviesView.as_view()),
    path('<slug:slug>/', MovieDetailView.as_view(), name='movie_detail')
]
