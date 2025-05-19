from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from .models import Product
from .tasks import add_product , remove_product

@receiver(post_save, sender=Product)
def handle_product_save(sender, instance, created, **kwargs):
    if created:
        print(f"[Product Created] {instance}")
        # add_product.delay(instance)
        add_product(instance.id)
    else:
        # remove_product.delay(instance.id)
        # add_product.delay(instance)
        remove_product(instance.id)
        add_product(instance.id)

        print(f"[Product Updated] {instance}")

@receiver(post_delete, sender=Product)
def handle_product_delete(sender, instance, **kwargs):
    print(f"[Product Deleted] {instance}")
    remove_product(instance.id)
