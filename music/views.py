from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse,Http404
from .models import Album,Song

def index(request):
    all_albums=Album.objects.all()
    return render(request,'music/index.html',{'albums':all_albums})


def detail(request,album_id):
    #try:
    #   album=Album.objects.get(pk=album_id)
    #except Album.DoesNotExist:
    #   raise Http404('Album does not exists!!!') 
    album=get_object_or_404(Album,pk=album_id)
    return render(request,'music/detail.html',{'album':album})

def favorite(request,album_id):
    album=get_object_or_404(Album,pk=album_id)
    try:
       sel_song=album.song_set.get(pk=request.POST['song'])
    except (KeyError,Song.DoesNotExist):
       return render(request,'music/detail.html',{'album':album, 'error_message':'Not a valid song'}) 
    else: 
       if sel_song.is_favorite:
          sel_song.is_favorite=False
          sel_song.save()
       else:
          sel_song.is_favorite=True
          sel_song.save()  
       return render(request,'music/detail.html',{'album':album} )
