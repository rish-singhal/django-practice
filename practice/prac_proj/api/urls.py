from django.urls import path
# from prac_proj.api.views import movie_list, movie_details
from prac_proj.api.views import MovieListAV, MovieDetailsAV

urlpatterns = [
    path('list/', MovieListAV.as_view(), name='movie-list'),
    path('<int:pk>', MovieDetailsAV.as_view(), name='movie-details'),
]
