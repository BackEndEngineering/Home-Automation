from django.http import HttpResponse
from .models import Gadget
from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
from django.template import loader
from .utils import calculate_age
from .forms import GadgetForm
from django.http import HttpResponseRedirect
from .forms import GadgetForm

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

def view_controller(request, guitron_id):
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

def index_componet(request):
    recent_componets = Componet.objects.all()
    context = {'componets': recent_componets}
    return render(request, 'guitron/componet_index.html', context)

def view_componet(request, componet_id):
    controller = get_object_or_404(Componet, id=controller_id)
    context = { 'controller': controller }
    return render(request, 'guitron/componet_details.html', context)
