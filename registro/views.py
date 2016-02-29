from django.shortcuts import render, render_to_response, redirect
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from .models import *
from .forms import  *


# Create your views here.

from django.http import HttpResponse
def home(request):
    return render_to_response('home.html')

def login(request):
    return render_to_response('login.html')

def asistente(request):
   if request.method == "POST":
      form = AsistenteForm(request.POST)
      if form.is_valid():
          registered = form.save()
          return redirect('/')
   else:
      form = AsistenteForm()
      return render(request, 'asistente.html', { 'form': form })