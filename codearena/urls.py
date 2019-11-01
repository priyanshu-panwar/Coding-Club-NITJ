from django.urls import path
from . import views

app_name = 'codearena'
urlpatterns = [
	path('', views.home, name='home'),
	path('post/<int:pk>/', views.post_detail, name='post-detail'),
]