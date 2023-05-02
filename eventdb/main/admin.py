from django.contrib import admin

from .models import Violations, Person, RelatedPerson

# Register your models here.

class PersonAdmin(admin.ModelAdmin):
    list_display = ['id', 'intruder_fio', 'sex', 'birthday', 'description', 'add_at']
admin.site.register(Violations)
admin.site.register(Person, PersonAdmin)
admin.site.register(RelatedPerson)