from django.contrib import admin
from .models import Album, Track

class TrackInline(admin.TabularInline):
    model = Track
    extra = 3
    fields = ['title', 'audio']


@admin.register(Album)
class AlbumAdmin(admin.ModelAdmin):
    list_display = ['title', 'artist', 'year']
    inlines = [TrackInline]


@admin.register(Track)
class TrackAdmin(admin.ModelAdmin):
    list_display = ['title', 'album']
    fields = ['title', 'album', 'audio']

class AlbumAdmin(admin.ModelAdmin):
    list_display = ['title', 'artist', 'year']
    fields = ['title', 'artist', 'year', 'info']
