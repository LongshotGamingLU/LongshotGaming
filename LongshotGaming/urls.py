"""LongshotGaming URL Configuration

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
from django.conf.urls import url
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', include('Homepage.urls')),
    path('user/', include('User.urls')),
    path('leaderboard/', include('Leaderboard.urls')),
    path('event-page/', include('EventPage.urls')),
    path('coming-soon/', include('ComingSoon.urls')),
    path('admin/', admin.site.urls),
    url(r'^oauth/', include('social_django.urls', namespace='social')),
    path('404/', views.page_not_found, name='handler404'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

handler404 = 'LongshotGaming.views.page_not_found'
handler500 = 'LongshotGaming.views.server_error'
