from urllib.parse import MAX_CACHE_SIZE
from django.db import models
from django.db.models import CASCADE
# импорт для получения абсолютного URL
from django.urls import reverse
# Create your models here.

# Группа
class Band(models.Model):
    band_id         = models.CharField(primary_key=True, unique=True, max_length=255)
    band_name       = models.CharField(max_length=255, db_index=True)
    band_slug       = models.SlugField(max_length=255, unique=True, null=True)
    band_genres     = models.CharField(max_length=255)
    band_URL        = models.URLField(max_length=255)
    band_followers  = models.SmallIntegerField(default=0)
    band_popularity = models.SmallIntegerField(default=0)
    band_image_300  = models.CharField(max_length=255)
    band_image_64   = models.CharField(max_length=255)
    band_created    = models.DateTimeField(auto_now_add=True)

    def get_absolute_url(self):
        return reverse('band_details', kwargs={'name': self.band_id})
    
    class Meta:
        ordering = ('band_name',)
        verbose_name = 'Группы'
        verbose_name_plural = 'Группы'

    def __str__(self) -> str:
        return f'{self.band_name}'


# Таблица Альбомов
class Album(models.Model):
    album_id           = models.CharField(primary_key=True, unique=True, max_length=255)
    album_name         = models.CharField(max_length=255, db_index=True)
    album_slug         = models.SlugField(max_length=255, unique=True, null=True)
    album_type_1       = models.CharField(max_length=255)
    album_type_2       = models.CharField(max_length=255)
    album_URL          = models.CharField(max_length=255)
    album_release_date = models.DateField(null=True)
    album_total_tracks = models.SmallIntegerField()
    album_image_300    = models.CharField(max_length=255, unique=False)
    album_image_64     = models.CharField(max_length=255, unique=False)
    band_id            = models.ForeignKey(Band,
                                           db_column          = 'band_id',
                                           related_name       = 'albums',
                                           on_delete          = CASCADE)
    band_name          = models.CharField(max_length=255)
    album_created      = models.DateTimeField(auto_now_add=True)

    def get_absolute_url(self):
        return reverse('tracks:tracks', args=[self.album_slug])

    class Meta:
        ordering = ('band_name', 'album_release_date', 'album_name',)
        verbose_name = 'Альбомы'
        verbose_name_plural = 'Альбомы'

    def __str__(self) -> str:
        return f'{self.band_name} - {self.album_name}'


# # Таблица треков
class Track(models.Model):
    track_id          = models.CharField(max_length=255, primary_key=True, unique=True)
    track_name        = models.CharField(max_length=255, db_index=True)
    track_slug        = models.SlugField(max_length=255, unique=True, null=True)
    track_disc_number = models.SmallIntegerField(default=1)
    track_number      = models.SmallIntegerField()
    track_duration    = models.IntegerField() 
    # статистика прослушиваний
    track_playcount   = models.SmallIntegerField(default=0)
    track_listeners   = models.SmallIntegerField(default=0)

    album_id        = models.ForeignKey(Album, 
                                       db_column          = 'album_id',
                                       related_name       = 'tracks', 
                                       on_delete          = CASCADE)
    album_name      = models.CharField(max_length=255)

    band_id         = models.ForeignKey(Band, 
                                       db_column          = 'band_id',
                                       related_name       = 'tracks',
                                       on_delete          = CASCADE)
    band_name       = models.CharField(max_length=255)
    
    track_image_300 = models.CharField(max_length=255)
    track_image_64  = models.CharField(max_length=255)
    track_preview   = models.CharField(max_length=255)
    track_URL       = models.CharField(max_length=255)
    # поля анализа
    track_danceability     = models.FloatField(default=0.)  
    track_energy           = models.FloatField(default=0.)
    track_key              = models.FloatField(default=0.)
    track_loudness         = models.FloatField(default=0.)
    track_mode             = models.FloatField(default=0.)
    track_speechiness      = models.FloatField(default=0.)
    track_acousticness     = models.FloatField(default=0.)
    track_instrumentalness = models.FloatField(default=0.)
    track_liveness         = models.FloatField(default=0.)
    track_valence          = models.FloatField(default=0.)
    track_tempo            = models.FloatField(default=0.)
    # сервисные поля
    track_created = models.DateTimeField(auto_now_add=True)

    def get_absolute_url(self):
        return reverse('web:tracks', args=[self.track_slug])

    class Meta:
        ordering = ('band_name', 'album_name', 'track_name',)
        verbose_name = 'Треки'
        verbose_name_plural = 'Треки'

    def __str__(self) -> str:
        return f'{self.band_name} - {self.track_name}'


# Тексты песен
class Text(models.Model):
    text_id      = models.AutoField(primary_key=True)
    text_slug    = models.SlugField(max_length=255, null=True)
    band_id      = models.CharField(max_length=255)
    band_name    = models.CharField(max_length=255)
    album_id     = models.CharField(max_length=255)
    album_name   = models.CharField(max_length=255)    
    track_id     = models.ForeignKey(Track, 
                                     db_column = 'track_id',
                                     on_delete=models.CASCADE)
    track_name   = models.CharField(max_length=255)    
    text_created = models.DateTimeField(auto_now_add=True)
    song_text    = models.TextField(null=True)

    # def get_absolute_url(self):
    #     return reverse('web:track_list_by_band', args=[self.slug])
    
    class Meta:
        ordering = ('band_name', 'album_name', 'track_name')
        verbose_name = 'Тексты песен'
        verbose_name_plural = 'Тексты песен'

    def __str__(self) -> str:
        return f'{self.band_name} - {self.track_name}'
 