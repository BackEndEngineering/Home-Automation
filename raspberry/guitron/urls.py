from django.conf.urls import url
from . import views

app_name = 'guitron'
urlpatterns = [
    url(r'^event/$', views.index, name='content-index')
]
