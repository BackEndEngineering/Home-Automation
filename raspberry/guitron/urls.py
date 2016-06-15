from django.conf.urls import url

from . import views

app_name = 'guitron'
urlpatterns = [
    url(r'^monitor/$', views.index, name="index"),
    url(r'^monitor/(?P<guitron_id>[0-9]+)/$', views.view_guitron, name='view')
]
