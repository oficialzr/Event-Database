from django.contrib import admin

from .models import Event, Person, RelatedPerson, AdressesPlacesOfBirth, AdressesPlacesOfLive, AdressesPlacesOfWork, OtherAdresses, Changes, ChangesEvent, FilesPerson, FilesEvent

# Register your models here.

class PersonAdmin(admin.ModelAdmin):
    list_display = ['id', 'fio', 'sex', 'birthday', 'description', 'add_at']
admin.site.register(Event)
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

