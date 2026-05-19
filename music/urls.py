from django.urls import path
from . import views

app_name = 'music'

urlpatterns = [
    path('', views.album_list, name='album_list'),
    path('album/<int:pk>/', views.album_detail, name='album_detail'),
    path('add/<int:track_id>/', views.add_to_library, name='add_to_library'),
    path('remove/<int:track_id>/', views.remove_from_library, name='remove_from_library'),
    path('library/', views.my_library, name='my_library'),
    path('random/', views.random_track, name='random_track'),
    path('search/', views.search_tracks, name='search_tracks'),
]