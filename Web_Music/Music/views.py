from django.shortcuts import render
from django.http import HttpResponse
from .models import Album,Song

def index(request):
    all_albums = Album.objects.all()
    context = {
        'all_albums':all_albums,
    }
    return render(request, 'music/index.html', context)

def details(request,album_id):
    return HttpResponse('<h2> Details for Album id : ' + str(album_id) + '</h2>')