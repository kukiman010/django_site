from django.urls import path, include
from . import views
from .views import *

urlpatterns = [
    path('', views.index, name='posts_list_url'),
    path('post/<str:slug>/', post_detail, name='post_detail_url'),
    path('tags/', tag_list, name='tags_list_url'),
    path('tag/<str:slug>', tag_detail, name='tag_detail_url')
]
