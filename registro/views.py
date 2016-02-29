from django.shortcuts import render, render_to_response
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from .models import *


# Create your views here.

from django.http import HttpResponse
def home(request):
    return render_to_response('home.html')

def login(request):
    return render_to_response('login.html')

def asistente(request):
   if request.method == "GET":
      form = NuevoAsistente()
      return render(request, 'asistente.html', { 'form': form })
   elif request.method == "POST":
      form = ArtistForm(request.POST)
      form.save()
      return HttpResp