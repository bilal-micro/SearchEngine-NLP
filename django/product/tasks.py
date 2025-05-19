from core.celery import app
from product.servicess.engine import Engine
from product.models import Product

@app.task
def setup_engine():
    Engine.train()
    return 0

@app.task
def add_product(id):
    Engine.add_new_product(Product.objects.get(id = id))
    return 0

@app.task
def remove_product(id):
    Engine.remove_product(id)
    return 0
