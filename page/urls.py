from django.urls import path
from . import views


urlpatterns = [
    path('',views.index, name='index'),
    path('social/',views.social, name='social'),
    path('entertainment/',views.entertainment, name='entertainment'),
    path('sport/',views.sport, name='sport'),
    path('technology/',views.technology, name='technology'),
    path('health/',views.health, name='health'),
    path('lifestyle/',views.lifestyle, name='lifestyle'),
]
