from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import LigneVente
from stock.models import Produit

@receiver(post_save, sender=LigneVente)
def soustraire_stock_apres_vente(sender, instance, created, **kwargs):
    if created:  # Vérifie si la ligne de vente vient d'être créée
        produit = instance.produit
        if produit.quantite_stock >= instance.quantite:
            produit.quantite_stock -= instance.quantite
            produit.save()
        else:
            raise ValueError(f"Stock insuffisant pour le produit {produit.nom}.")