from django.contrib import admin

from .models import Event, Person, RelatedPerson, AdressesPlacesOfBirth, AdressesPlacesOfLive, AdressesPlacesOfWork, OtherAdresses, Changes, ChangesEvent, FilesPerson, FilesEvent
from .models import Entity, Division, Filial, Representation
from .models import Logging, LoggingUser

# Register your models here.

class PersonAdmin(admin.ModelAdmin):
    list_display = ['id', 'fio', 'sex', 'birthday', 'description', 'add_at']
    ordering = ['id']

class EventAdmin(admin.ModelAdmin):
    list_display = ['id', 'type', 'date_incedent', 'entity', 'division', 'filial', 'representation', 'change_date']
    ordering = ['-change_date']

class Log(admin.ModelAdmin):
    list_display = ['author', 'type', 'datetime']
    readonly_fields=('datetime',)

admin.site.register(Event, EventAdmin)
admin.site.register(Person, PersonAdmin)
admin.site.register(RelatedPerson)

admin.site.register(AdressesPlacesOfBirth)
admin.site.register(AdressesPlacesOfLive)
admin.site.register(AdressesPlacesOfWork)
admin.site.register(OtherAdresses)

admin.site.register(Changes)
admin.site.register(ChangesEvent)

admin.site.register(FilesPerson)
admin.site.register(FilesEvent)

admin.site.register(Entity)
admin.site.register(Division)
admin.site.register(Filial)
admin.site.register(Representation)

admin.site.register(Logging, Log)
admin.site.register(LoggingUser, Log)


