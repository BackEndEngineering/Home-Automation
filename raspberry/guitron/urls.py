from django.conf.urls import url

from . import views

app_name = 'guitron'
urlpatterns = [
    url(r'^light/$', views.action_form, name='light'),
    url(r'^get_action/$', views.get_action, name='get_action'),
    url(r'^component/$', views.index_component, name="component"),
    url(r'^component/(?P<component_id>[0-9]+)/$', views.view_component, name='component'),
    url(r'^dashboard/$', views.dashboard, name="dashboard"),
    url(r'^events/$', views.index_event, name="events"),
    url(r'^events/(?P<event_id>[0-9]+)/$', views.view_event, name='events'),
    url(r'^controllers/$', views.index_controller, name="controllers"),
    url(r'^controllers/(?P<controller_id>[0-9]+)/$', views.view_controller, name='controllers'),
    url(r'^event/$', views.create_event, name="event"),
    url(r'^create_event/$', views.create_event, name='create_event'),
    url(r'^gadget/$', views.index, name="index"),
    url(r'^gadget/(?P<guitron_id>[0-9]+)/$', views.view_guitron, name='view'),
    url(r'^contact_form/$', views.contact_form, name="contact_form"),
    url(r'^create/$', views.create_form, name='create')
]
