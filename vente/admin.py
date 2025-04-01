from django.contrib import admin
from .models import Vente, LigneVente

class LigneVenteInline(admin.TabularInline):
    model = LigneVente
    extra = 1
    readonly_fields = ('prix_unitaire', 'total')  # Afficher le total par ligne dans l'inline

@admin.register(Vente)
class VenteAdmin(admin.ModelAdmin):
    list_display = ('id', 'date_vente', 'client', 'utilisateur', 'total_vente')  # Ajouter le total de la vente
    inlines = [LigneVenteInline]

    def total_vente(self, obj):
        return f"{obj.total_vente:.2f} €"  # Formater le total avec deux décimales
    total_vente.short_description = "Total de la vente"  # Nom de la colonne dans l'admin
