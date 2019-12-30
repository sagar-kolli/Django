from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home(request):
    return render(request, 'home.html', {})

def services(request):
    return render(request, 'Services.html', {})	
	
def about(request):
    return render(request, 'About.html', {})
def pegaInstance(request):
    return render(request, 'pegaInstance.html', {})
def kubernetes(request):
    return render(request, 'kubernetes.html', {})
def upgrade(request):
    return render(request, 'upgrade.html', {})
def login(request):
    return render(request, 'login.html', {})