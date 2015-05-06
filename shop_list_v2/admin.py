from django.contrib import admin

# Register your models here.
from shop_list_app2.models import User, Product, Group, Order, Phone

class UserAdmin(admin.ModelAdmin):
    list_display = ['id','email','name','active','created_at','modified_at']
    list_filter = ['active','created_at']

class ProductAdmin(admin.ModelAdmin):
    list_display = ['id','name','active','avatar','measure','created_at','modified_at']
    list_filter = ['active','created_at']

class PhoneAdmin(admin.ModelAdmin):
    list_display = ['id','id_device','active','os','created_at','modified_at']
    list_filter = ['active','created_at']

class GroupAdmin(admin.ModelAdmin):
    list_display = ['id','name','avatar','active','created_at','modified_at']
    list_filter = ['active','created_at']

class OrderAdmin(admin.ModelAdmin):
    list_display = ['id','name','active','created_at','modified_at']
    list_filter = ['active','created_at']

admin.site.register(User, UserAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Phone, PhoneAdmin)
admin.site.register(Group, GroupAdmin)
admin.site.register(Order, OrderAdmin)