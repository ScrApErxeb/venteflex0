from django.contrib import admin
from django.utils.html import format_html
from django.urls import path
from django.shortcuts import get_object_or_404, redirect
from django.contrib import messages
from .models import Facture, Paiement

@admin.register(Facture)
class FactureAdmin(admin.ModelAdmin):
    list_display = ('id', 'bouton_paiement', 'vente', 'montant_total','date_emission',  'est_payee')
    list_filter = ('est_payee', 'date_emission')
    search_fields = ('vente__client',)

    def bouton_paiement(self, obj):
        if not obj.est_payee:
            return format_html(
                '<a class="button" href="{}">Marquer comme payée</a>',
                f"/admin/compta/facture/{obj.id}/marquer_payee/"
            )
        return "Payée"
    bouton_paiement.short_description = "Action"

    def get_urls(self):
        urls = super().get_urls()
        custom_urls = [
            path(
                '<int:facture_id>/marquer_payee/',
                self.admin_site.admin_view(self.marquer_comme_payee_view),
                name='compta_facture_marquer_payee',
            ),
        ]
        return custom_urls + urls

    def marquer_comme_payee_view(self, request, facture_id):
        facture = get_object_or_404(Facture, id=facture_id)

        if facture.est_payee:
            messages.warning(request, f"La facture #{facture.id} est déjà marquée comme payée.")
        else:
            # Marquer la facture comme payée
            facture.est_payee = True
            facture.save()

            # Enregistrer un paiement correspondant
            Paiement.objects.create(
                facture=facture,
                montant=facture.montant_total,
                mode_paiement='CASH'  # Par défaut, mode de paiement en espèces
            )

            messages.success(request, f"La facture #{facture.id} a été marquée comme payée et un paiement a été enregistré.")

        return redirect(f"/admin/compta/facture/{facture_id}/change/")

@admin.register(Paiement)
class PaiementAdmin(admin.ModelAdmin):
    list_display = ('id', 'facture', 'date_paiement', 'montant', 'mode_paiement')
    list_filter = ('mode_paiement', 'date_paiement')
    search_fields = ('facture__vente__client',)
