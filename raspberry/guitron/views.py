from django.http import HttpResponse
from .models import Monitor
from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
from django.template import loader
from .utils import calculate_age

def index(request):
    recent_monitors = Monitor.objects.all()
    context = {'recent_monitors': recent_monitors}
    return render(request, 'guitron/guitron_index.html', context)

def view_guitron(request, guitron_id):
    monitor = get_object_or_404(Monitor, id=monitor_id)
    context = { 'monitor': monitor }

    return render(request, 'guitron/guitron_details.html', context)
