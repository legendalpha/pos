from django.db import models
from django.conf import settings  # To access User model if needed
from inventory.models import Product

class SalesOrder(models.Model):
    order_id = models.CharField(max_length=50, unique=True, blank=True)  # Changed to blank
    # customer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True)  # Link to User (if applicable)  
    date_created = models.DateTimeField(auto_now_add=True) 
    status = models.ForeignKey('sales.OrderStatus', on_delete=models.PROTECT, default=1)  # Assuming you create a 'New' status as default
    total_amount = models.DecimalField(max_digits=10, decimal_places=2,default=0)   
    cash_tendered = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)  
    customer_name = models.CharField(max_length=100, default='Customer')

    def save(self, *args, **kwargs):
        if not self.pk:
            prefix = 'INV'
            qs = SalesOrder.objects.all().order_by('-order_id') 
            if qs.exists():
                last_order_id = qs.first().order_id
                last_number = int(last_order_id[3:])  
                new_order_id = prefix + str(last_number + 1).zfill(7) 
            else:
                new_order_id = prefix + '0000001' 
            self.order_id = new_order_id
            print("Order ID:", self.order_id)
        super(SalesOrder, self).save(*args, **kwargs)
    

class SalesOrderItem(models.Model):
    order = models.ForeignKey(SalesOrder, on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    quantity = models.IntegerField(default=1)
    price = models.DecimalField(max_digits=10, decimal_places=2)  # Unit price
    # ... additional fields (discount, etc.) if needed ...

class OrderStatus(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name
