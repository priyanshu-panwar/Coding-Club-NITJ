from django.urls import path
from . import views

app_name = 'core'
urlpatterns = [
	path('', views.home, name='home'),
	path('contact/', views.contact, name='contact'),
	path('subscribe/', views.subscription, name='subscribe'),
]