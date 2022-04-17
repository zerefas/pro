from .models import Movie


def movie_slider(request):

    movie = Movie.objects.all().order_by('created_date')[0:5]
    return {'slider_movies':movie}