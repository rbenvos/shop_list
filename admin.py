from django.contrib import admin

# Register your models here.
from shop_list_app.models import User, Product

class UserAdmin(admin.ModelAdmin):
    list_display = ['email','active','id_tlf_and','created_at','modified_at']
    list_filter = ['active','created_at']

class ProductAdmin(admin.ModelAdmin):
    list_display = ['name','active','created_at','modified_at']
    list_filter = ['active','created_at']

admin.site.register(User, UserAdmin)
admin.site.register(Product, ProductAdmin)