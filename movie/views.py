from django.shortcuts import render
from django.views.generic import ListView,DetailView
from django.views.generic.dates import YearArchiveView
from .models import *
# Create your views here.(class base view)


class HomeView(ListView):
    model = Movie
    template_name = 'movie/home.html'

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        context['top_rated'] = self.model.objects.filter(status = 'top')
        context['recently_watched'] = self.model.objects.filter(status = 'recently')
        context['most_watched'] = self.model.objects.filter(status = 'most')

        return context


class MovieList(ListView):
    model= Movie
    paginate_by = 2


class MovieDetails(DetailView):
    model = Movie

    def get_object(self):
        object = super(MovieDetails, self).get_object()
        object.view_count +=1
        object.save()
        return object


    def get_context_data(self, **kwargs):
        context = super(MovieDetails, self).get_context_data(** kwargs)
        context['links'] = Movielink.objects.filter(movie=self.get_object())
        context['related_movies'] = Movie.objects.filter(category =self.get_object().category)
        return context





class MovieCategory(ListView):
    model = Movie
    paginate_by = 2


    def get_queryset(self):
        self.category = self.kwargs['category']
        movies = Movie.objects.filter(category = self.category)
        return movies


    def get_context_data(self,**kwargs):
        context =super(MovieCategory, self).get_context_data(**kwargs)
        context['movie_category'] =self.category
        return context


class MovieLanguage(ListView):
    model = Movie
    paginate_by = 2


    def get_queryset(self):
        self.language = self.kwargs['language']
        movies = Movie.objects.filter(language = self.language)
        return movies


    def get_context_data(self,**kwargs):
        context =super(MovieLanguage, self).get_context_data(**kwargs)
        context['movie_language'] =self.language
        return context



class MovieSearch(ListView):
    model = Movie
    paginate_by = 2


    def get_queryset(self):
        query = self.request.GET.get('q')
        if query:
           object_list = Movie.objects.filter(title__icontains=query)
        else:
           object_list =self.objects.none()

        return object_list

class MovieYear(YearArchiveView):
    queryset = Movie.objects.all()
    date_field = 'year_of_production'
    make_object_list = True
    allow_future = True