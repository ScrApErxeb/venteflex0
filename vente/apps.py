from django.apps import AppConfig


class VenteConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'vente'

    def ready(self):
        import vente.signals  # Importer les signaux
