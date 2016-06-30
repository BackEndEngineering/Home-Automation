"""raspberry URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
import guitron
from . import views
from django.conf import settings
from django.conf.urls.static import static
from rest_framework import routers
from guitron.api import UserViewSet, ControllerViewSet
from guitron import views

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)
router.register(r'Controller', views.ControllerViewSet)
router.register(r'Event', views.EventViewSet)
router.register(r'Component', views.ComponentViewSet)

urlpatterns = [
     url(r'^', include('django.contrib.auth.urls')),
     url(r'^$', views.dashboard, name="dashboard"),
     url(r'^guitron/', include('guitron.urls')),
     url(r'^admin/', admin.site.urls),
     url(r'^api/', include(router.urls)),
     url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
