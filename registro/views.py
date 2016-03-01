from django.shortcuts import render, render_to_response, redirect
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from .models import *
from .forms import  *
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.template import RequestContext
from django.contrib.auth import views

def home(request):
    return render(request, 'home.html')

def userprofile(request):
    return render(request, 'userprofile.html')

def asistentes(request):

   if request.method == "POST":
      if 'find' in request.POST:
          return HttpResponseRedirect ('/asistente/' + request.POST.get('cedula'))
      elif 'new' in request.POST:
          form = AsistenteForm(request.POST)
          if form.is_valid():
            registered = form.save()
            return HttpResponseRedirect ('/asistente/' + request.POST.get('cedula'))
      else:
          return HttpResponseRedirect ('/')
   else:
      form = AsistenteForm()
      return render(request, 'asistente.html', { 'form': form })

def asisdata(request, id):

    try:
        asisdata = Asistente.objects.get(pk = id)
        return render_to_response('Asisdata.html', { 'asisdata': asisdata})
    except:
        return render (request, 'nomatch.html')
