from django.contrib.auth.models import User
from rest_framework import serializers, viewsets
from .models import Controller, Componet, Event


# Serializers define the API representation.
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'is_staff')

class ControllerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Controller
        fields = ('name', 'location', 'user')

class EventSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Event
        fields = ('componet', 'time', 'value')

class ComponetSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Componet
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

class ComponetViewSet(viewsets.ModelViewSet):
    queryset = Componet.objects.all()
    serializer_class = ComponetSerializer
