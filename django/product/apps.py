from django.apps import AppConfig


class ProductConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'product'
    def ready(self):
        from product.tasks import setup_engine
        setup_engine.delay()
        import product.signals

        return super().ready()