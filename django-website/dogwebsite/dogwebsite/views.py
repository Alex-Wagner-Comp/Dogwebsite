from django.http import HttpResponse, HttpResponseRedirect, Http404, FileResponse
from django.shortcuts import render, redirect
from django.views.generic.base import TemplateView
from django.db import models
from .forms import createDogForm, createApptForm
from .model import Dog

def index(request):
    return render(request, "index.html")

def profile(request):
    return render(request, "profile.html")

def createDog(request):
    form = createDogForm()
    if request.method == 'POST':
        form = createDogForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/index/')

    return render(request, 'accounts/adddog.html', {'form' : form})

def createAppt(request):
    form = createApptForm()
    if request.method == 'POST':
        form = createApptForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/index/')

    return render(request, 'accounts/appt.html', {'form' : form})

def showdata(request):
    data = Dog.objects.all()
    return render(request, 'accounts/showdatabase.html', {'data' : data})

def downloaddata(request):
    file_path = 'db.sqlite3'
    response = FileResponse(open('db.sqlite3', 'rb'), as_attachment=True)
    return response


class ProfileView(TemplateView):
    template_name = 'accounts/profile.html'