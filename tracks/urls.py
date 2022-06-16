from gettext import bind_textdomain_codeset
from django.urls import path
from .views import *


urlpatterns = [
    path('', index),
    path('bands/', bands, name='bands'),
    path('bands/<str:band_id>/', band_details, name='band_details'),
    
    
]