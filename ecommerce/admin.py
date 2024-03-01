from django.contrib import admin
from .models import *

# Register your models here.
# admin.site.register(product)
@admin.register(Product)
class ProductAdmin (admin.ModelAdmin):
    list_display = ['name','price','quantity','description']

admin.site.register(Cart)

class OrderDetailInline(admin.TabularInline):
    model = OrderDetail
    extra = 0
    readonly_fields=('product', 'quantity','unit_price','total_price')

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    inlines = [OrderDetailInline]
    readonly_fields=('name','total_order_price','user','phone_number','address')
    list_display= ['name' ,'total_order_price', 'status']