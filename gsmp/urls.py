
from django.contrib import admin
from django.urls import path

from gsmp import views
from . import views
from gsmp.views import index, events

app_name = "gsmp"


urlpatterns = [
    path('', views.index, name="home"),
    path('about/', views.about, name="about"),
    path('director_board/', views.director_board, name="director_board"),
    path('advisory_board/', views.advisory_board, name="advisory_board"),
    path('who_we_are/', views.who_we_are, name="who_we_are"),
    path('history/', views.history, name="history"),
    # path('news/', views.index, name="news"),
    path('events/', views.index, name="events"),
    path('resources/', views.resources, name="resources"),
    path('members/', views.members, name="members"),
    path('mission/', views.mission, name="mission"),

]


