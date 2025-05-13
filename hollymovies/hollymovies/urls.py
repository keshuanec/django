"""
URL configuration for hollymovies project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls.i18n import urlpatterns
from django.contrib import admin
from django.shortcuts import render
from django.urls import path, include
from django.conf.urls import handler403
from django.conf.urls.i18n import i18n_patterns # import umožní překlady
from django.conf import settings
from django.conf.urls.static import static
from viewer.views import (hello, ahoj, index,
                          movie_index, actor_index,
                          movie_detail, actor_detail,
                          director_detail, MovieView, ProfileView, RegistrationView,
                          MovieCreateView, ActorCreateView, ActorDetailView, ActorUpdateView, ActorDeleteView, MovieDetailView, MovieUpdateView,
                          MovieDeleteView)


"""
urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello/<parametr>', hello),
    path('ahoj/', ahoj),
    path('', index, name="index"),
    path('movies', movie_index, name="movies"),
    path('actors', actor_index, name="actors"),
    #path('movie_detail', movie_detail, name="movie_detail"),
    #path('actor_detail', actor_detail, name="actor_detail"),
    path('director_detail', director_detail, name="director_detail"),
    #movies
    path('movie_create', MovieCreateView.as_view(), name="movie_create"),
    path('movie/<int:pk>/', MovieDetailView.as_view(), name="movie_detail"),
    path('movie/update/<int:pk>/', MovieUpdateView.as_view(), name="movie_update"),
    path('movie/delete/<int:pk>/', MovieDeleteView.as_view(), name="movie_delete"),

    #actors
    path('actor_create', ActorCreateView.as_view(), name="actor_create"),
    path('actors/update/<int:pk>/', ActorUpdateView.as_view(), name="actor_update"),
    path('actor/<int:pk>/', ActorDetailView.as_view(), name="actor_detail"),
    path('actor/delete/<int:pk>/', ActorDeleteView.as_view(), name="actor_delete"),

    #urls for auth
    path('accounts/', include("django.contrib.auth.urls")),
    path('accounts/profile', ProfileView.as_view(), name="profile"),
    path('registration', RegistrationView.as_view(),name="registration")
]
"""

def permission_denied(request, exception=None):
    return render(request, "403.html", status=403)

handler403 = permission_denied

urlpatterns = i18n_patterns(
    path('i18n/', include('django.conf.urls.i18n')),
    path('admin/', admin.site.urls),
    path('hello/<parametr>', hello),
    path('ahoj/', ahoj),
    path('', index, name="index"),
    path('movies', movie_index, name="movies"),
    path('actors', actor_index, name="actors"),
    #path('movie_detail', movie_detail, name="movie_detail"),
    #path('actor_detail', actor_detail, name="actor_detail"),
    path('director_detail', director_detail, name="director_detail"),
    #movies
    path('movie_create', MovieCreateView.as_view(), name="movie_create"),
    path('movie/<int:pk>/', MovieDetailView.as_view(), name="movie_detail"),
    path('movie/update/<int:pk>/', MovieUpdateView.as_view(), name="movie_update"),
    path('movie/delete/<int:pk>/', MovieDeleteView.as_view(), name="movie_delete"),

    #actors
    path('actor_create', ActorCreateView.as_view(), name="actor_create"),
    path('actors/update/<int:pk>/', ActorUpdateView.as_view(), name="actor_update"),
    path('actor/<int:pk>/', ActorDetailView.as_view(), name="actor_detail"),
    path('actor/delete/<int:pk>/', ActorDeleteView.as_view(), name="actor_delete"),

    #urls for auth
    path('accounts/', include("django.contrib.auth.urls")),
    path('accounts/profile', ProfileView.as_view(), name="profile"),
    path('registration', RegistrationView.as_view(),name="registration")
)
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)