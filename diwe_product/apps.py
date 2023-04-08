from django.apps import AppConfig


class DiweProductConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'diwe_product'

    def ready(self):
        import diwe_product.signals
