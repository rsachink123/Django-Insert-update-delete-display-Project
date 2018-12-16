from django.contrib import admin
from .models import Product

class AdminProduct(admin.ModelAdmin):
    list_display = ['productid','productname','productcost','productcolor','productweight']
admin.site.register(Product,AdminProduct)
