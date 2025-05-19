from django.apps import AppConfig
import threading

class ProductConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'product'
    def ready(self):
        from product.tasks import setup_engine
        # setup_engine.delay()
        threading.Thread(target=setup_engine).start()
        import product.signals

        return super().ready()