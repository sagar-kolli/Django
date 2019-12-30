from django.shortcuts import render
from django.http import HttpResponse
import sys
from subprocess import run,PIPE

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
def exteral(request):
    out = run([sys.executable,'C:\\Users\\kolls2\\Desktop\\Sagar\\Django\\test.py'],shell=False,stdout=PIPE)
    return render(request, 'external.html', {'data': out.stdout})