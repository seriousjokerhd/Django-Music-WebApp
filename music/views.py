from django.shortcuts import render, get_object_or_404
from .models import Album, Song


def index(request):
    albums = Album.objects.all()
    return render(request, 'music/index.html', {'albums': albums})


def detail(request, album_id):
        album = get_object_or_404(Album, pk=album_id)
        return render(request, 'music/details.html', {'album': album})


def favorite(request, album_id):
    album = get_object_or_404(Album, pk=album_id)
    try:
        song_selected = album.song_set.get(pk=request.POST['song'])
    except (Song.DoesNotExist, KeyError):
        return render(request, 'music/details.html', {'album': album, 'error_message': 'You did something wrong'})

    else:
        song_selected.is_favorite = True
        song_selected.save()
        return render(request, 'music/details.html', {'album': album})




