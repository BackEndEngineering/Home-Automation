from django.http import HttpResponse
from .models import Gadget, Controller, Event, Component, Action
from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
from django.template import loader
from .utils import calculate_age
from .forms import GadgetForm, ActionForm
from django.http import HttpResponseRedirect
from .forms import GadgetForm
from rest_framework import viewsets
from django.contrib.auth.models import User, Group
from guitron.api import UserSerializer, GroupSerializer, ControllerSerializer, EventSerializer, ComponentSerializer, ActionSerializer
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

def get_action(request):
    actions = Action.objects.filter(completed=False)
    for action in actions:
        action.completed=True
        action.save()
    serializer = ActionSerializer(actions, many=True, context={'request': request})
    return JsonResponse({'actions': serializer.data})

def action_form(request):
    if request.method == 'POST':
        component = Component.objects.get(id=1)
        if 'ON' in request.POST:
            Action.objects.create(
                component = component,
                value = 'ON',
                completed = False)
        elif 'OFF' in request.POST:
            Action.objects.create(
                component = component,
                value = 'OFF',
                completed = False)



    context = {}
    return render(request, 'guitron/lights.html', context)



def dashboard(request):
    recent_controllers = Controller.objects.all()
    recent_events = Event.objects.order_by('-time')[0:5]
    context = {'recent_controllers': recent_controllers, 'recent_events': recent_events}
    return render(request, 'guitron/dashboard.html', context)


def index(request):
    recent_gadgets = Gadget.objects.all()
    context = {'recent_gadgets': recent_gadgets}
    return render(request, 'guitron/guitron_index.html', context)

def view_guitron(request, guitron_id):
    gadget = get_object_or_404(Gadget, id=guitron_id)
    context = { 'gadget': gadget }
    return render(request, 'guitron/guitron_details.html', context)

def create_form(request):
    if request.method == 'POST':
        form = GadgetForm(request.POST)
        if form.is_valid():
            gadget = form.save()
            return HttpResponseRedirect('/guitron/gadget/' + str(gadget.id))
    else:
        form = GadgetForm()

    return render(request, 'guitron/create_gadget.html', {'form': form})

def contact_form(request):
    if request.method == 'POST':
        form = GadgetForm(request.POST)
        if form.is_valid():
            # do stuff here; fields are in form.cleaned_data
            return HttpResponseRedirect('/guitron/')
    else:
        form = GadgetForm()

    return render(request, 'guitron/contact.html', {'form': form})

def view_image(request, image_id):
    image = get_object_or_404(Image, id=image_id)
    response = FileResponse(open(image.image.url, 'rb'), content_type='image/' + image_type)
    context = { 'image': image }
    return render(request, 'guitron/image_details.html', context)

def index_controller(request):
    recent_controllers = Controller.objects.all()
    context = {'recent_controllers': recent_controllers}
    return render(request, 'guitron/controller_index.html', context)

def view_controller(request, controller_id):
    controller = get_object_or_404(Controller, id=controller_id)
    context = { 'controller': controller }
    return render(request, 'guitron/controller_details.html', context)


def index_event(request):
    recent_events = Event.objects.all()
    context = {'recent_events': recent_events}
    return render(request, 'guitron/event_index.html', context)

def view_event(request, event_id):
    event = get_object_or_404(Event, id=event_id)
    context = { 'event': event}
    return render(request, 'guitron/event_details.html', context)

def index_component(request):
    recent_components = Component.objects.all()
    context = {'recent_components': recent_components}
    return render(request, 'guitron/component_index.html', context)

def view_component(request, component_id):
    component = get_object_or_404(Component, id=component_id)
    context = { 'component': component }
    return render(request, 'guitron/component_details.html', context)

def view_image(request, image_id):
    image = get_object_or_404(Image, id=image_id)
    response = FileResponse(open(image.image.url, 'rb'), content_type='image/' + image_type)
    context = { 'image': image }
    return render(request, 'guitron/image_details.html', context)

class ActionViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Action.objects.all()
    serializer_class = ActionSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer

class ControllerViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Controller.objects.all().order_by('-date_joined')
    serializer_class = ControllerSerializer

class EventViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Event.objects.all().order_by('-date_joined')
    serializer_class = EventSerializer

class ComponentViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Component.objects.all().order_by('-date_joined')
    serializer_class = ComponentSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

class ControllerViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Controller.objects.all()
    serializer_class = ControllerSerializer

class EventViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Event.objects.all()
    serializer_class = EventSerializer

class ComponentViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Component.objects.all()
    serializer_class = ComponentSerializer

@csrf_exempt
def create_event(request):
    event_data = None
    if request.method == 'POST':
        event_data = json.loads(str(request.body.decode('utf-8')))

    else:
        return event_data

    controller = Controller.objects.get(uuid=event_data['uuid'])
    comps = Component.objects.filter(
            controller = controller,
            pin = int(event_data['pin']))

    component = None
    if comps:
        component = comps[0]
    else:
        component = Component.objects.create(
            controller = controller,
            pin = int(event_data['pin']),
            name = event_data['name'],
            area = event_data['area'],
            kind = event_data['kind']
        )

    event = Event.objects.create(
        component = component,
        value = event_data['value']
        )

    return JsonResponse({'create_event': event.id})
