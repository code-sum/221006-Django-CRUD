from django.shortcuts import render, redirect
from .forms import MovieForm

# Create your views here.

def index(request):
    return render(request, 'movies/index.html')

def create(request):
    if request.method == 'POST':
        movie_form = MovieForm(request.POST)
        if movie_form.is_valid():
            movie_form.save()
            return redirect('movies:index')
    else:
        movie_form = MovieForm()
    context = {
        'movie_form': movie_form
    }
    return render(request, 'movies/new.html', context=context)