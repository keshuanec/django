from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from viewer.models import Movie, Actor, Director

from django.views.generic import ListView, TemplateView, DetailView, FormView, UpdateView, DeleteView
from django.contrib.auth.models import User, Group      # group je pro opravněni
from .forms import RegistrationForm, MovieForm, ActorForm


# Create your views here.

def hello(request, parametr):
    return HttpResponse(f"Hello {parametr} World!")

def ahoj(request):
    hodnota = request.GET.get('hodnota', '')
    hodnota2 = request.GET.get('hodnota2', '')
    return HttpResponse(f"data od uživatele jsou {hodnota} a {hodnota2}")

def index(request):
    return render(request, 'index.html')

def movie_index(request):
    movies = Movie.objects.all()
    return render(request, 'movies/index.html', context={"movies" : movies})

def actor_index(request):
    actors = Actor.objects.all()
    return render(request, 'actors/index.html', context={"actors" : actors})

def movie_detail(request):
    movie_id = int(request.GET.get('movie_id', ''))
    movie = Movie.objects.get(id=movie_id)
    return render(request, 'movies/detail.html', context={"movie" : movie})

def actor_detail(request):
    actor_id = int(request.GET.get('actor_id', ''))
    actor = Actor.objects.get(id=actor_id)
    return render(request, 'actors/detail.html', context={"actor" : actor})

def director_detail(request):
    director_id = int(request.GET.get('director_id', ''))
    director = Director.objects.get(id=director_id)
    return render(request, 'directors/detail.html', context={"director" : director})



"""
classBased Views
"""



class MovieView(ListView):
    model = Movie
    template_name = 'movies/index.html'

class MovieDetailView(DetailView):
    model = Movie
    template_name = 'movies/detail.html'

class ActorDetailView(DetailView):
    model = Actor
    template_name = 'actors/detail.html'

class ActorUpdateView(PermissionRequiredMixin, UpdateView):
    template_name = 'actors/edit.html'
    form_class = ActorForm
    success_url = reverse_lazy('actors')
    model = Actor
    permission_required =  'viewer.change_actor'

    # oprávnění se píše ve tvaru - názevaplikace.názevoperace_názevmodelu
    # složitější oprávnění - middleware

class ActorDeleteView(PermissionRequiredMixin, DeleteView):
    model = Actor
    template_name = 'actors/delete.html'
    success_url = reverse_lazy('actors')
    permission_required =  'viewer.delete_actor'

class ActorCreateView(PermissionRequiredMixin, FormView):
    template_name = 'actors/create.html'
    form_class = ActorForm
    success_url = 'actors'
    permission_required = 'viewer.create_actor'

    def form_valid(self, form):
        actor = Actor(
            name=form.cleaned_data['name'],
            surname=form.cleaned_data['surname'],
            birth_day=form.cleaned_data['birth_day'],
            image_url=form.cleaned_data['image_url'],
        )
        actor.save()
        return super().form_valid(form)

class MovieUpdateView(PermissionRequiredMixin, UpdateView):
    template_name = 'movies/edit.html'
    form_class = MovieForm
    success_url = reverse_lazy('movies')
    model = Movie
    permission_required = 'viewer.change_movie'


class MovieDeleteView(PermissionRequiredMixin, DeleteView):
    model = Movie
    template_name = 'movies/delete.html'
    success_url = reverse_lazy('movies')
    permission_required = 'viewer.delete_movie'

class MovieCreateView(PermissionRequiredMixin, FormView):
    template_name = 'movies/create.html'
    form_class = MovieForm
    success_url = 'movies'
    permission_required = 'viewer.create_movie'

    def form_valid(self, form):
        movie = Movie(
            title=form.cleaned_data['title'],
            rating=form.cleaned_data['rating'],
            released=form.cleaned_data['released'],
            description=form.cleaned_data['description'],
            poster_url=form.cleaned_data['poster_url'],
            genre_id=form.cleaned_data['genre_id'].id,
            director_id=form.cleaned_data['director'].id,
        )
        movie.save()

        actors = form.cleaned_data['actor_ids']
        movie.actor.set(actors)

        return super().form_valid(form)



class ProfileView(LoginRequiredMixin, DetailView):
    model = User
    context_object_name = "user_profile"

    def get_object(self):
        return self.request.user

    template_name = "accounts/profile.html"


class RegistrationView(FormView):
    template_name = 'registration/registration.html'
    form_class = RegistrationForm
    success_url = 'accounts/profile'

    def form_valid(self, form):
        user = form.save()

        group = Group.objects.get(name='default_user')
        user.groups.add(group)  #groups je z modelu User

        return super().form_valid(form)


"""
GET: /formular?jmeno=Petr&heslo=tajneheslo  (neni uplne fajn)
GET: 127.0.0.1:8000/ahoj?hodnota=test
POST: /formular  lepsi, neukazuje data
"""