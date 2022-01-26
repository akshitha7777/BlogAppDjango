from nturl2path import url2pathname

from App.models import Post
from . import views
from django.urls import path

urlpatterns = [
  path('', views.PostList.as_view(), name="home"),
  path('<slug:slug>/', views.PostList.as_view(), name="post_detail"),
]