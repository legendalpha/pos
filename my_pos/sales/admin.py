from django.contrib import admin
from .models import SalesOrder, SalesOrderItem, OrderStatus

import logging
logger = logging.getLogger(__name__)  # Create a logger specific to your admin module
from django import forms

class SalesOrderItemInline(admin.TabularInline):
    model = SalesOrderItem
    extra = 1
    def save_model(self, request, obj, form, change):
        print("save_model method called!")
        print("Change:", change)
        print("Order status:", obj.order.status)
        print("Order status name:", obj.order.status.name)
        super().save_model(request, obj, form, change)
        if change and obj.order.status.name == 'In Progress':
            print("Updating order status to 'In Progress'")
            obj.order.status = OrderStatus.objects.get(name='In Progress')
            obj.order.save()
            
class SalesOrderAdmin(admin.ModelAdmin):
    inlines = [SalesOrderItemInline]
    readonly_fields = ('order_id',)  # Display order ID in admin but don't allow editing
    fields = ('status',)

admin.site.register(SalesOrder, SalesOrderAdmin)

admin.site.register(OrderStatus)
