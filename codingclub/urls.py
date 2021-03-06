"""codingclub URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from blog.views import PostListView


admin.site.site_header = "Coding Club NITJ"
admin.site.site_title = "Coding Club NITJ Portal"
admin.site.index_title = "Welcome to Coding Club NITJ Portal"


urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('authenticate.urls', namespace='authenticate')),
    path('', include('core.urls', namespace='core')),
    path('blog/', include('blog.urls', namespace='blog')),
    path('tag/(?P<slug>[\w-]+)/$', PostListView.as_view(), name='tagged'),
    path('startup/', include('startup.urls', namespace='startup')),
    path('codearena/', include('codearena.urls', namespace='codearena')),
    path('meeting/', include('meeting.urls', namespace='meeting')),

    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/', include('allauth.urls')),
    path('api/v1/', include('social_django.urls', namespace='social')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
