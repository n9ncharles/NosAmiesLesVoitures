from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

from boutique.models import Voiture


# Create your views here.
def index(request):
    voitures = Voiture.objects.all()
    return render(request, 'index.html', {"voitures": voitures})


def detail(request, slug):
    details = get_object_or_404(Voiture, slug=slug)
    return render(request, 'detail.html', {"details": details})