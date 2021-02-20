from django.contrib import admin
from FoodApp.models import Product, Cart, OrderTable
# Register your models here.


class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'pname', 'price', 'category', 'description']
    list_editable = ('price', 'description')


admin.site.register(Product, ProductAdmin)


class CartAdmin(admin.ModelAdmin):
    list_display = ['id', 'pid', 'price', 'quantity', 'total', 'user']

    # list_editable=['quantity']
admin.site.register(Cart, CartAdmin)


class OrderTableAdmin(admin.ModelAdmin):
    list_display = ['pid', 'name', 'quantity',
                    'price', 'user', 'date', 'status', 'detail']
    list_editable = ['status', 'detail']


admin.site.register(OrderTable, OrderTableAdmin)
