from django.contrib import admin
from .models import Produit, MouvementStock, Categorie

@admin.register(Produit)
class ProduitAdmin(admin.ModelAdmin):
    list_display = ('nom', 'categorie', 'prix', 'quantite_stock')
    list_filter = ('categorie',)
    search_fields = ('nom', 'categorie__nom')

@admin.register(MouvementStock)
class MouvementStockAdmin(admin.ModelAdmin):
    list_display = ('produit', 'type_mouvement', 'quantite', 'date_mouvement')
    list_filter = ('type_mouvement', 'produit__categorie')
    search_fields = ('produit__nom',)

@admin.register(Categorie)
class CategorieAdmin(admin.ModelAdmin):
    list_display = ('nom', 'description')
    search_fields = ('nom',)
