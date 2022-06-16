from django.http import HttpResponse
from django.shortcuts import render
from tracks.models import *

# Create your views here.
from django.http import HttpResponse

def index(request):
    context = {
        'title': 'Russian Rock Playlist',
    }
    return render(request, 'tracks/index.html', context=context)

# def index(request):
#     return HttpResponse('Главная страница')

def bands(request):
    context = {
        'title': 'Все исполнители',
        'bands': Band.objects.all().order_by('-band_popularity')[:10],
    }
    return render(request, 'tracks/bands.html', context=context)

def band_details(request, name):
    return HttpResponse(f'Исполнитель {name}')

    # return HttpResponse('Все исполнители')

# def albums(request):
#     return HttpResponse('Все альбомы')


# def tracks(request):
#     return HttpResponse('Все треки')
