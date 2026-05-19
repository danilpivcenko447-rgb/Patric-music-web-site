from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Album, Track, UserLibrary
import random
from django.db.models import Q
def album_list(request):
    return render(request, 'music/album_list.html', {'albums': Album.objects.all()})

def album_detail(request, pk):
    album = get_object_or_404(Album, pk=pk)
    user_track_ids = []
    if request.user.is_authenticated:
        user_track_ids = UserLibrary.objects.filter(user=request.user).values_list('track_id', flat=True)
    return render(request, 'music/album_detail.html', {
        'album': album,
        'tracks': album.tracks.all(),
        'user_track_ids': user_track_ids,
    })

@login_required
def add_to_library(request, track_id):
    UserLibrary.objects.get_or_create(user=request.user, track_id=track_id)
    return redirect(request.META.get('HTTP_REFERER', 'music:album_list'))

@login_required
def remove_from_library(request, track_id):
    UserLibrary.objects.filter(user=request.user, track_id=track_id).delete()
    return redirect(request.META.get('HTTP_REFERER', 'music:album_list'))

@login_required
def my_library(request):
    return render(request, 'music/my_library.html', {
        'user_tracks': UserLibrary.objects.filter(user=request.user).select_related('track__album')
    })

def random_track(request):
    tracks = list(Track.objects.all())
    if not tracks:
        return render(request, 'music/random_track.html', {'error': 'Нет треков'})
    track = random.choice(tracks)
    return render(request, 'music/random_track.html', {'track': track})
def search_tracks(request):

    query = request.GET.get('q', '')
    tracks = []
    if query:
        tracks = Track.objects.filter(
            Q(title__icontains=query) | Q(album__artist__icontains=query)
        ).select_related('album')
    return render(request, 'music/search_results.html', {'tracks': tracks, 'query': query})