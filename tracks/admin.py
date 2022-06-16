from re import search
from django.contrib import admin
from django.forms import models

# Register your models here
from tracks.models import *



@admin.register(Band)
class BandAdmin(admin.ModelAdmin):
    list_display  = ['band_name', 'band_followers', 'band_popularity',]
    search_fields = ['band_name',]
    prepopulated_fields = {'band_slug': ('band_name',)}


@admin.register(Album)
class AlbumAdmin(admin.ModelAdmin):
    list_display  = ['band_name', 'album_name',]
    list_filter   = ['band_name', 'album_name',]
    search_fields = ['band_name', 'album_name',]
    prepopulated_fields = {'album_slug': ('album_name',)}


@admin.register(Track)
class TrackAdmin(admin.ModelAdmin):
    list_display  = ['band_name', 'album_name', 'track_name', 'track_listeners', 'track_playcount',]
    list_filter   = ['band_name', 'album_name', 'track_name',]    
    search_fields = ['band_name', 'track_name',]
    prepopulated_fields = {'track_slug': ('track_name',)}


@admin.register(Text)
class TextAdmin(admin.ModelAdmin):
    list_display  = ['band_name', 'track_name',]
    list_filter   = ['band_name', 'track_name',]
