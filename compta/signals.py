from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from vente.models import Vente, LigneVente
from .models import Facture, Paiement

@receiver(post_save, sender=Vente)
def creer_facture_apres_vente(sender, instance, created, **kwargs):
    """
    Crée une facture automatiquement après la création d'une vente.
    """
    if created:  # Vérifie si la vente vient d'être créée
        Facture.objects.create(
            vente=instance,
            est_payee=False  # Par défaut, la facture est marquée comme impayée
        )


@receiver(post_save, sender=LigneVente)
def mettre_a_jour_facture_apres_modification_ligne(sender, instance, **kwargs):
    """
    Met à jour le montant total de la facture après modification ou ajout d'une ligne de vente.
    """
    vente = instance.vente
    if hasattr(vente, 'facture'):  # Vérifie si une facture existe pour cette vente
        facture = vente.facture
        # Pas besoin de recalculer ici car `montant_total` est une propriété dynamique
        facture.save()  # Appeler save() pour déclencher d'autres actions si nécessaire


@receiver(post_delete, sender=LigneVente)
def mettre_a_jour_facture_apres_suppression_ligne(sender, instance, **kwargs):
    """
    Met à jour le montant total de la facture après suppression d'une ligne de vente.
    """
    vente = instance.vente
    if hasattr(vente, 'facture'):  # Vérifie si une facture existe pour cette vente
        facture = vente.facture
        facture.save()  # Appeler save() pour refléter les changements


@receiver(post_save, sender=Facture)
def creer_paiement_apres_facture_payee(sender, instance, **kwargs):
    """
    Crée un paiement automatiquement après qu'une facture est marquée comme payée.
    """
    if instance.est_payee:  # Vérifie si la facture est marquée comme payée
        # Vérifier si un paiement existe déjà pour cette facture
        if not Paiement.objects.filter(facture=instance).exists():
            Paiement.objects.create(
                facture=instance,
                montant=instance.montant_total,  # Utilise le montant total de la facture
                mode_paiement='CASH'  # Par défaut, mode de paiement en espèces
            )