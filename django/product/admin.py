from django.contrib import admin
from .models import Product

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'category', 'brand', 'price', 'created_at')
    search_fields = ('title', 'category', 'brand')
    list_filter = ('category', 'brand', 'created_at')
    ordering = ('-created_at',)
