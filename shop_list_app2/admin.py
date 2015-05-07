from django.contrib import admin

# Register your models here.
from shop_list_app2.models import User, Product, Group, Order, Phone

class UserAdmin(admin.ModelAdmin):
    fieldsets = (
        ('User information', {
            'fields': [('name', 'last_name'), 'email', 'password','avatar','active']
        }),
        ('Device', {
            'classes': ('wide',),
            'fields': ['device']
        }),
        ('Friends', {
            'classes': ('collapse',),
            'fields': ['friends']
        }),
    )
    list_display = ['id','active','email','name','last_name','getNumFriendsActive','getNumDevices','created_at','modified_at']
    list_display_links = ['name', 'last_name','email']
    list_filter = ['id','email','name','last_name','active','created_at','modified_at']
    search_fields = ['id','name', 'last_name','email']
    actions=['make_active','make_desactive']

    def make_active(modeladmin, request, queryset):
        queryset.update(active = True)
    make_active.short_description = "Mark selected as active"

    def make_desactive(modeladmin, request, queryset):
        queryset.update(active = False)
    make_desactive.short_description = "Mark selected as desactive"


    #sacar en que grupo esta un usuario

class ProductAdmin(admin.ModelAdmin):
    list_display = ['id','active','name','quantity','measure','created_at','modified_at','avatar']
    list_filter = ['active','created_at']

class PhoneAdmin(admin.ModelAdmin):
    list_display = ['id','id_device','active','os','userPhone','created_at','modified_at']
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