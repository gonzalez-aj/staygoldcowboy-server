"""
URL configuration for staygoldcowboy project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.conf.urls import include
from rest_framework import routers
from django.contrib import admin
from django.urls import path
from django.urls import path
from staygoldcowboyapi.views import (
        register_user,
        check_user,
        ArtView,
        TagView
    )

router = routers.DefaultRouter(trailing_slash=False)
router.register(r'arts', ArtView, 'art')
router.register(r'tags', TagView, 'tag')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register', register_user),
    path('checkuser', check_user),
    path('', include(router.urls)),
]
