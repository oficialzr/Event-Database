from django.contrib import admin

from .models import Violations, Intruder, Witness, Injured

# Register your models here.

admin.site.register(Violations)
admin.site.register(Intruder)
admin.site.register(Witness)
admin.site.register(Injured)