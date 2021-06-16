from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect
from .models import Author, FairyTale

# Create your views here.


def home(request):
    return render(request, "website/homepage.html",
                  {"tales": FairyTale.objects.all()})


def tales(request):
    return render(request, "website/tales.html",
                  {"tales": FairyTale.objects.all()})


def authors(request):
    return render(request, "website/authors.html")


def content(request, id):
    tale = get_object_or_404(FairyTale, pk=id)
    return render(request, "website/content.html",
                  {"tale": tale})



