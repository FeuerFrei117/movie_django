from django.urls import path

from movies.views import MoviesView, MovieDetailView, FilterMoviesView, AddReview

app_name = 'movies'

urlpatterns = [
    path('', MoviesView.as_view()),
    path('filter/', FilterMoviesView.as_view(), name='filter'),
    path('<slug:slug>/', MovieDetailView.as_view(), name='movie_detail'),
    path('review/<int:pk>/', AddReview.as_view(), name='add_review')
]
