from django.contrib import admin
from .models import Audio, Contact, Partnership


class ParnershipAdmin(admin.ModelAdmin):
    search_fields = ["name"]
    list_display = ["name", "phone_number"]

# Register your models here.
admin.site.register(Audio)
admin.site.register(Contact)
admin.site.register(Partnership, ParnershipAdmin)