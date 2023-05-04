from django.contrib import admin
from django.urls import path

from .views import addEvent, eventView
from .views import startPage, loginView, logoutView
from .views import personsView, eventsView
from .views import personView
from .views import addPersonSolo
from .views import searchPerson

from .views import get_request, delete_person, check_person, createRelations


urlpatterns = [
    path('', startPage, name='home'),
    path('login/', loginView, name='login'),
    path('logout/', logoutView, name='login'),


    path('events/', eventsView, name='events'),
    path('persons/', personsView, name='persons'),
    path('injureds/', personsView, {'role': 'injureds'}, name='injureds'),
    path('witnesses/', personsView, {'role': 'witnesses'}, name='witnesses'),
    path('intruders/', personsView, {'role': 'intruders'}, name='intruders'),

    path('add-person/', addPersonSolo, name='add-person'),
    path('add-event/', addEvent, name='add-event'),
    path('create-relations/<slug:event_id>', createRelations, name='create-relations'),

    path('event/<int:event_id>', eventView, name='event'),
    path('person/<int:person_id>', personView, name='person'),

    path('search/', searchPerson),

    path('add-person-on-event/<slug:id>', get_request),
    path('delete-person/<slug:id>', delete_person),
    path('check-person/<slug:id>', check_person),
]