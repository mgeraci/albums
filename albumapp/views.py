from django.shortcuts import render, get_object_or_404
from albumapp.models import Album, AlbumList, AlbumSelection, AlbumLink


def album_lists(request):
  lists = AlbumList.objects.all()
  context = {'lists': lists}
  return render(request, 'album_lists.html', context)


def album_list(request, slug):
  lists = AlbumList.objects.all()
  list = get_object_or_404(AlbumList, slug=slug)
  selections = AlbumSelection.objects.filter(album_list=list)

  context = {
    'lists': lists,
    'list': list,
    'selections': selections,
  }

  return render(request, 'album_list.html', context)
