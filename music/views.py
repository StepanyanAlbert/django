from django.shortcuts import render
from django.http import HttpResponse,Http404
from .models import Album

def index(request):
    all_albums=Album.objects.all()
    return render(request,'music/index.html',{'albums':all_albums})


def detail(request,album_id):
    try:
       album=Album.objects.get(pk=album_id)
    except Album.DoesNotExist:
       raise Http404('Album does not exists!!!') 
    return render(request,'music/detail.html',{'album':album})
