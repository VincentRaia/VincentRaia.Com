from django.contrib import admin

# Register your models here.
from django.contrib import admin
from landing.models import Land

class LandingAdmin(admin.ModelAdmin):
    list_display = ['object_title']
    # enable the save buttons on top of change form
    save_on_top = True

admin.site.register(Land, LandingAdmin)