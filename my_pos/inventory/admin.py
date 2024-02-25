from django.contrib import admin
from .models import Product, Supplier # Import your Product model

admin.site.register(Product)


admin.site.register(Supplier)