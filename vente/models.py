from django.db import models
from stock.models import Produit
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

class Vente(models.Model):
    date_vente = models.DateTimeField(auto_now_add=True)
    client = models.CharField(max_length=255, blank=True, null=True)
    utilisateur = models.ForeignKey(User, on_delete=models.CASCADE, related_name="ventes")

    def __str__(self):
        return f"Vente #{self.id} - {self.date_vente}"

    @property
    def total_vente(self):
        # Calculer le total de toutes les lignes de vente associées
        return sum(ligne.total for ligne in self.lignes.all())


class LigneVente(models.Model):
    vente = models.ForeignKey(Vente, on_delete=models.CASCADE, related_name="lignes")
    produit = models.ForeignKey(Produit, on_delete=models.CASCADE, related_name="lignes_vente")
    quantite = models.PositiveIntegerField()
    prix_unitaire = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)

    def clean(self):
        # Vérifier si le prix de vente du produit est défini
        if self.produit.prix_vente is None:
            raise ValidationError(f"Le produit {self.produit.nom} n'a pas de prix de vente défini.")

        # Vérifier si le prix de vente est inférieur au prix d'achat
        if self.produit.prix_vente < self.produit.prix_achat:
            raise ValidationError(
                f"Le prix de vente ({self.produit.prix_vente}) du produit {self.produit.nom} est inférieur au prix d'achat ({self.produit.prix_achat})."
            )

    def save(self, *args, **kwargs):
        # Définir automatiquement le prix unitaire à partir du prix de vente du produit
        if self.prix_unitaire is None:
            self.prix_unitaire = self.produit.prix_vente
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.produit.nom} (x{self.quantite})"

    @property
    def total(self):
        # Gérer les cas où quantite ou prix_unitaire est None
        if self.quantite is None or self.prix_unitaire is None:
            return 0
        return self.quantite * self.prix_unitaire