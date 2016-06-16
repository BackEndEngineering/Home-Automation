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
