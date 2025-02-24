from django.urls import path, include
from .views import *
from . import views





app_name = "online_encyclopedia"


urlpatterns = [
    path('', views.term_list, name='online_encyclopedia_home'),
    path('<slug:slug>/', views.term_detail, name='online_encyclopedia_details'),
    path("get-terms/", get_terms, name="get_terms"),
    path("get-term-definition/<slug:slug>/", get_term_definition, name="get_term_definition"),

]