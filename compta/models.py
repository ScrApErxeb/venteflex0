from django.db import models
from vente.models import Vente

class Facture(models.Model):
    vente = models.OneToOneField(Vente, on_delete=models.CASCADE, related_name="facture")
    date_emission = models.DateTimeField(auto_now_add=True)
    est_payee = models.BooleanField(default=False)

    @property
    def montant_total(self):
        # Calculer le montant total à partir des lignes de vente associées
        return sum(ligne.total for ligne in self.vente.lignes.all())

    def __str__(self):
        return f"Facture #{self.id} - {self.vente.client} ({'Payée' if self.est_payee else 'Non payée'})"


class Paiement(models.Model):
    facture = models.ForeignKey(Facture, on_delete=models.CASCADE, related_name="paiements")
    date_paiement = models.DateTimeField(auto_now_add=True)
    montant = models.DecimalField(max_digits=10, decimal_places=2)
    mode_paiement = models.CharField(max_length=50, choices=[
        ('CASH', 'Espèces'),
        ('CARD', 'Carte bancaire'),
        ('TRANSFER', 'Virement bancaire'),
    ])

    def __str__(self):
        return f"Paiement #{self.id} - {self.montant} € ({self.mode_paiement})"
