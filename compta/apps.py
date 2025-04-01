from django.apps import AppConfig

class ComptaConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'compta'

    def ready(self):
        import compta.signals  # Importer les signaux
