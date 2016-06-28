from django.shortcuts import render

def index(request):
    return render(request, 'guitron/dashboard.html')
