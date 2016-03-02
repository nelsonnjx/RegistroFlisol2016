from django.shortcuts import render, render_to_response, redirect
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from .models import *
from .forms import  *
from reportlab.pdfgen import canvas
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

          if Asistente.objects.filter(pk = request.POST.get('cedula')).exists():
              form = AsistenteForm()
              return render(request, 'asistente.html', { 'form': form , 'error_msg': True})

          else:
              form = AsistenteForm(request.POST)
              if form.is_valid():
                registered = form.save()
                return HttpResponseRedirect ('/asistente/' + request.POST.get('cedula'))
      else:
          return HttpResponseRedirect ('/')
   else:
      form = AsistenteForm()
      return render(request, 'asistente.html', { 'form': form })

def edit_asistente(request, id):
   edit_idnumber = id
   edit_asist = Asistente.objects.get(pk = id)

   if request.method == "POST":

#CHECK IF ID ISN'T THE SAME

      if request.POST.get('cedula') != edit_idnumber:

#CHECK IF ID IS ANYWHERE ELSE

             if Asistente.objects.filter(pk = request.POST.get('cedula')).exists():
                form = AsistenteForm(instance=edit_asist)
                return render(request, 'edit_asistente.html', { 'form': form, 'error_msg': True })

#NO OTHER MATCHES

             else:
                form = AsistenteForm(request.POST, instance=edit_asist)
                if form.is_valid():
                   registered = form.save()
                   Asistente.objects.get(pk = id).delete()

                   return HttpResponseRedirect ('/asistente/' + request.POST.get('cedula'))


                else:
                    print("Error 2 Reached")
                    return HttpResponseRedirect ('/login/')

      else:
             form = AsistenteForm(request.POST, instance=edit_asist)
             if form.is_valid():
                registered = form.save()
                return HttpResponseRedirect ('/asistente/' + request.POST.get('cedula'))

             else:
                    print("Error 3 Reached")
                    return HttpResponseRedirect ('/login/')


   else:
      form = AsistenteForm(instance=edit_asist)
      return render(request, 'edit_asistente.html', { 'form': form })

#def edit_asistente(request, id):

#   edit_asist = Asistente.objects.get(pk = id)
#   if request.method == "POST":
#          form = AsistenteForm(request.POST, instance=edit_asist)
#          if form.is_valid():
#             registered = form.save()
#             return HttpResponseRedirect ('/asistente/' + request.POST.get('cedula'))
#          else:
#             return HttpResponseRedirect ('/login/')
#   else:
#      form = AsistenteForm(instance=edit_asist)
#      return render(request, 'edit_asistente.html', { 'form': form, })

def asisdata(request, id):

    try:
        asisdata = Asistente.objects.get(pk = id)
        return render_to_response('Asisdata.html', { 'asisdata': asisdata})
    except:
        return render (request, 'nomatch.html')

def comprobante(request, id):

    try:
        comprobante = Asistente.objects.get(pk = id)
        return render_to_response('comprobante.html', { 'comprobante': comprobante})
    except:
        return None