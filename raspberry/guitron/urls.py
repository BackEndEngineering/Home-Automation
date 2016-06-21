from django.conf.urls import url

from . import views

app_name = 'guitron'
urlpatterns = [
    url(r'^event/$', views.add_event, name="event")
    url(r'^gadget/$', views.index, name="index"),
    url(r'^gadget/(?P<guitron_id>[0-9]+)/$', views.view_guitron, name='view'),
    url(r'^contact_form/$', views.contact_form, name="contact_form"),
    url(r'^create/$', views.create_form, name='create')
]
