from django.db import models

class Product(models.Model):
    sku = models.CharField(max_length=50, unique=True)  # Stock Keeping Unit
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock_quantity = models.IntegerField(default=0)
    purchase_price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)  
    sales_price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    mrp = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    discount_percent = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    barcode = models.CharField(max_length=50, unique=True, null=True, blank=True)
    category = models.ForeignKey('Category', on_delete=models.PROTECT, null=True, blank=True) 
    image = models.ImageField(upload_to='product_images', null=True, blank=True) 
    # ... inside your Product model ...
    supplier = models.ForeignKey('Supplier', on_delete=models.SET_NULL, null=True, blank=True) 

    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=100)
    parent_category = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='subcategories') 

    def __str__(self):
        return self.name 

class Supplier(models.Model):
    name = models.CharField(max_length=200)
    contact_person = models.CharField(max_length=100)
    email = models.EmailField(blank=True)
    phone_number = models.CharField(max_length=20, blank=True)
    address = models.TextField(blank=True) 
    supplier_id = models.IntegerField(default=0)

class Customer(models.Model):
    name = models.CharField(max_length=200)
    contact_person = models.CharField(max_length=100)
    email = models.EmailField(blank=True)
    phone_number = models.CharField(max_length=20, blank=True)
    address = models.TextField(blank=True) 
    customer_id = models.IntegerField(default=0)

