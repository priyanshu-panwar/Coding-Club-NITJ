from django.urls import path
from .views import (
    PostListView,
    PostListView2,
    #PostDetailView,
    #PostCreateView,
    PostUpdateView,
    #PostDeleteView,
    UserPostListView,
)
from . import views
import re

app_name = 'blog'
urlpatterns = [
    path('', views.home, name='home'),
    #path('', PostListView.as_view(), name='home'),
    path('user/<str:username>', UserPostListView.as_view(), name='user-posts'),
    path('post/<int:pk>/', views.post_detail, name='post-detail'),
    #path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/new/', views.post_create, name='post-create'),
    #path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', views.post_delete, name='post-delete'),
    #path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
]