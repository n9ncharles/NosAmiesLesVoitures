from django.contrib import admin

from boutique.models import Voiture


class VoitureAdmin(admin.ModelAdmin):
    list_display = ("marque", "serie", "categorie", "immatriculation")
    search_fields = ["categorie", "immatriculation"]


# Register your models here.
admin.site.register(Voiture, VoitureAdmin)
