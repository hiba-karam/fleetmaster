from django.contrib import admin
from .models import Modele, Vehicule, Maintenance

# Register your models here.

class VehiculeAdmin(admin.ModelAdmin):
    list_display = ('immatriculation', 'modele', 'kilometrage', 'etat', 'date_fabrication')
    list_filter = ('etat', 'modele', 'date_fabrication')
    search_fields = ('immatriculation',)
    list_editable = ('kilometrage', 'etat')
    
admin.site.register(Modele)
admin.site.register(Vehicule, VehiculeAdmin)
admin.site.register(Maintenance)