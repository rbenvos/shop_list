from django.contrib import admin
from shop_list_app2.models import User, Product, Group, Order, Phone, Item
from import_export import resources
from import_export.admin import ImportExportModelAdmin

"""
Administracion User
"""

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
    list_display = ['id','active','email','name','last_name','getNumFriendsActive','getNumDevices','getNumGroups','created_at','modified_at']
    list_display_links = ['name', 'last_name','email']
    list_filter = ['active','created_at','modified_at']
    search_fields = ['id','name', 'last_name','email']
    actions=['make_active','make_desactive']

    def make_active(modeladmin, request, queryset):
        queryset.update(active = True)
    make_active.short_description = "Mark selected as active"

    def make_desactive(modeladmin, request, queryset):
        queryset.update(active = False)
    make_desactive.short_description = "Mark selected as desactive"


"""
Administracion Product
"""
class ProductResource(resources.ModelResource):
    class Meta:
        model = Product
        exclude = ('active','avatar','quantity','measure','created_at','modified_at')

class ProductAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ['id','active','avatar','name','quantity','measure','created_at','modified_at']
    list_display_links = ['id','name','avatar']
    list_filter = ['active','created_at','modified_at']

    fieldsets = (
        ('Product information', {
            'fields': ['name', 'active','avatar']
        }),
        ('Units measure', {
            'classes': ('wide',),
            'fields': ['quantity','measure']
        }),
    )
    search_fields = ['id','name', 'last_name','email']
    actions=['make_active','make_desactive']

    #Importador - Exportador
    resource_class = ProductResource

    #Funciones
    def make_active(modeladmin, request, queryset):
        queryset.update(active = True)
    make_active.short_description = "Mark selected as active"

    def make_desactive(modeladmin, request, queryset):
        queryset.update(active = False)
    make_desactive.short_description = "Mark selected as desactive"


"""
Administracion Phone
"""
class PhoneAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Device information', {
            'fields': ['id_device', 'active', 'os']
        }),
    )
    list_display = ['id','id_device','active','os','numUsers','created_at','modified_at']
    list_filter = ['active','created_at']
    list_display_links = ['id', 'id_device']
    search_fields = ['id','id_device', 'numUsers']
    actions=['make_active','make_desactive']

    def make_active(modeladmin, request, queryset):
        queryset.update(active = True)
    make_active.short_description = "Mark selected as active"

    def make_desactive(modeladmin, request, queryset):
        queryset.update(active = False)
    make_desactive.short_description = "Mark selected as desactive"


"""
Administracion Group
"""
class GroupAdmin(admin.ModelAdmin):
    list_display = ['id','name','avatar','active','groupUsers','groupOrders','created_at','modified_at']
    list_display_links = ['id','name','avatar']
    list_filter = ['active','created_at','modified_at']

    fieldsets = (
        ('Group information', {
            'fields': ['name', 'active','avatar']
        }),
        ('Users information', {
            'classes' : ['wide'],
            'fields': ['users']
        }),
        ('Order information', {
            'classes' : ['wide'],
            'fields': ['orders']
        }),
    )
    search_fields = ['id','name']
    actions=['make_active','make_desactive']

    def make_active(modeladmin, request, queryset):
        queryset.update(active = True)
    make_active.short_description = "Mark selected as active"

    def make_desactive(modeladmin, request, queryset):
        queryset.update(active = False)
    make_desactive.short_description = "Mark selected as desactive"

"""
Administracion Order
"""
class OrderAdmin(admin.ModelAdmin):
    list_display = ['id','name','active','getGroups','orderNumProducts','created_at','modified_at']
    list_display_links = ['id','name']
    list_filter = ['active','created_at','modified_at']

    fieldsets = (
        ('Order information', {
            'fields': ['name', 'active']
        }),
        ('Products information', {
            'classes' : ['wide'],
            'fields': ['items']
        }),
    )
    search_fields = ['id','name']
    actions=['make_active','make_desactive']

    def make_active(modeladmin, request, queryset):
        queryset.update(active = True)
    make_active.short_description = "Mark selected as active"

    def make_desactive(modeladmin, request, queryset):
        queryset.update(active = False)
    make_desactive.short_description = "Mark selected as desactive"

"""
Administracion Order
"""
class ItemAdmin(admin.ModelAdmin):
    list_display = ['id','active','purchased','amount','product','getOrder','created_at','modified_at']
    list_display_links = ['id']
    list_filter = ['active','purchased','created_at','modified_at']
    actions=['make_active','make_desactive']

    def make_active(modeladmin, request, queryset):
        queryset.update(active = True)
    make_active.short_description = "Mark selected as active"

    def make_desactive(modeladmin, request, queryset):
        queryset.update(active = False)
    make_desactive.short_description = "Mark selected as desactive"

admin.site.register(User, UserAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Phone, PhoneAdmin)
admin.site.register(Group, GroupAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(Item, ItemAdmin)