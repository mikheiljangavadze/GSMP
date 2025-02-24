from django.urls import path
from .views import *
from . import views


app_name = "mp_news"

urlpatterns = [
    path('', NewsHome.as_view(), name='newshome'),
    path('category/<str:slug>/', PostsByCategory.as_view(), name='category'),
    path('tag/<str:slug>/', PostsByTag.as_view(), name='tag'),
    path('post/<str:slug>/', GetPost.as_view(), name='post'),
    path('search/', Search.as_view(), name='search'),
    path('post/<slug:post_id>/add_comment/', views.add_comment, name='add_comment'),
    path('post/<str:slug>/pdf/', views.post_pdf_view, name='post_pdf'),
]