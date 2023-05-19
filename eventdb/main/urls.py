from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static

from django.conf import settings

from .views import addEvent
from .views import startPage, loginView, logoutView
from .views import personsView, eventsView
from .views import personView, eventView, changeView
from .views import addPerson, addAdress
from .views import searchPerson, add_person_with_redirect

from .views import add_person_on_event, edit_person, edit_event


urlpatterns = [
    path('', startPage, name='home'),
    path('login/', loginView, name='login'),
    path('logout/', logoutView, name='login'),


    path('events/', eventsView, name='events'),
    path('persons/', personsView, name='persons'),

    path('add-person/', addPerson, name='add-person'),
    path('add-event/', addEvent, name='add-event'),
    path('add-adress/<int:person_id>', addAdress, name='add-adress'),

    path('event/<int:event_id>', eventView, name='event'),
    path('person/<int:person_id>', personView, name='person'),
    path('change/<int:change_id>', changeView, name='change'),

    path('search/', searchPerson),

    path('add-person-on-event/<slug:id>', add_person_on_event, name='add-person-on-event'),
    path('add-person-redirect/', add_person_with_redirect, name='add-person-redicrect'),

    path('edit-person/<int:id_person>', edit_person, name='edit-person'),
    path('edit-event/<int:id_event>', edit_event, name='edit-event'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
