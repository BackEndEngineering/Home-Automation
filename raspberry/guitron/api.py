from django.contrib.auth.models import User, Group
from rest_framework import serializers, viewsets
from .models import Controller, Component, Event


# Serializers define the API representation.
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'is_staff')

class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')

class ControllerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Controller
        fields = ('name', 'location', 'user', 'uuid')

class EventSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Event
        fields = ('component', 'time', 'value')

class ComponentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Component
        fields = ('name', 'area', 'kind', 'controller', 'pin')


# ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class ControllerViewSet(viewsets.ModelViewSet):
    queryset = Controller.objects.all()
    serializer_class = ControllerSerializer

class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer

class ComponentViewSet(viewsets.ModelViewSet):
    queryset = Component.objects.all()
    serializer_class = ComponentSerializer
