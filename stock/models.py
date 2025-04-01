from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.db import models

class Categorie(models.Model):
    nom = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.nom


class Produit(models.Model):
    nom = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    prix = models.DecimalField(max_digits=10, decimal_places=2)
    quantite_stock = models.PositiveIntegerField()
    categorie = models.ForeignKey(Categorie, on_delete=models.CASCADE, related_name="produits")

    def __str__(self):
        return self.nom


from django.contrib.auth.models import User
from django.db import models

class MouvementStock(models.Model):
    TYPE_MOUVEMENT = [
        ('ENTREE', 'Entrée'),
        ('SORTIE', 'Sortie'),
    ]

    produit = models.ForeignKey(Produit, on_delete=models.CASCADE, related_name="mouvements")
    type_mouvement = models.CharField(max_length=10, choices=TYPE_MOUVEMENT)
    quantite = models.PositiveIntegerField()
    date_mouvement = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="mouvements_stock")

    def clean(self):
        if self.type_mouvement == 'SORTIE' and self.quantite > self.produit.quantite_stock:
            raise ValidationError(f"La quantité de sortie ({self.quantite}) dépasse le stock disponible ({self.produit.quantite_stock}).")

    def save(self, *args, **kwargs):
        self.clean()
        if self.type_mouvement == 'ENTREE':
            self.produit.quantite_stock += self.quantite
        elif self.type_mouvement == 'SORTIE':
            self.produit.quantite_stock -= self.quantite
        self.produit.save()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.type_mouvement} - {self.produit.nom} ({self.quantite})"