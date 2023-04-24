from django.contrib import admin
from django.urls import path, include

from .views import startPage, injuredsView, intrudersView, witnessView, intruderPersonView, witnessPersonView, injuredPersonView, addSoloIntruder, addIntruder, addEvent, searchIntruder, eventView, addWitness, addInjured
from .views import editIntruder


urlpatterns = [
    path('', startPage, name='home'),
    path('injureds', injuredsView, name='injureds'),
    path('witnesses', witnessView, name='witnesses'),
    path('intruders', intrudersView, name='intruders'),



    path('add-intruder/', addIntruder, name='add-intruder'),
    path('add-event/', addEvent, name='add-event'),
    path('add-witness/', addWitness, name='add-witness'),
    path('add-injured/', addInjured, name='add-injured'),
    path('add-solo-intruder', addSoloIntruder, name='add-solo-intruder'),

    path('event/<int:event_id>', eventView, name='event'),
    path('injured/<int:injured_id>', injuredPersonView, name='injured'),
    path('witness/<int:witness_id>', witnessPersonView, name='witness'),
    path('intruder/<int:intruder_id>', intruderPersonView, name='intruder'),

    path('intruder-update/<int:intruder_id>', editIntruder, name='intruder-update'),




    path('search/', searchIntruder),
]