# -*- coding: utf-8 -*-

from django.shortcuts import render
from models import User, Group,Product, Order, Phone, Item
from forms import UserForm, GroupForm, OrderForm,PhoneForm,ProductForm
from django.views.generic import View, ListView

"""
DASHBOARD
"""

def dashboard(request):
    db_users_list = User.objects.all().order_by("-created_at")[:5]
    db_groups_list = Group.objects.all().order_by("-created_at")[:5]
    db_devices_list = Phone.objects.all().order_by("-created_at")[:5]
    db_orders_list = Order.objects.all().order_by("-created_at")[:5]
    db_items_list = Item.objects.all().order_by("-created_at")[:5]
    db_products_list = Product.objects.all().order_by("-created_at")[:5]
    context = {'db_users_list': db_users_list,
               'db_groups_list': db_groups_list,
               'db_devices_list': db_devices_list,
               'db_orders_list': db_orders_list,
               'db_items_list': db_items_list,
               'db_products_list': db_products_list,
               }
    return render(request, 'dashboard.html',context)


"""
LISTS
"""
class NewUserView(View):

    def get(self, request):
        users = User.objects.all()
        form = UserForm()
        success_message = ''
        context = {'form': form, 'message': success_message,'users_list': users}
        return render(request, 'lists/users_list.html', context)

    def post(self, request):
        users = User.objects.all()
        success_message = ""
        form = UserForm()
        if request.method == 'POST':
            form = UserForm(request.POST)
            if form.is_valid():
                form.save()
                success_message = "Usuario guardado"
                form = UserForm()

        context = {'form': form, 'message': success_message,'users_list': users}
        return render(request, 'lists/users_list.html', context)

class NewDeviceView(View):
    def get(self, request):
        devices = Phone.objects.all()
        form = PhoneForm()
        success_message = ''
        context = {'form': form, 'message': success_message,'devices_list': devices}
        return render(request, 'lists/devices_list.html', context)

    def post(self, request):
        devices = Phone.objects.all()
        success_message = "Dispositivo creado"
        form = PhoneForm()
        if request.method == 'POST':
            form = PhoneForm(request.POST)
            if form.is_valid():
                form.save()
                success_message = '''
                <p style="color:green">
                    Guardado con exito!
                </p>
                '''
                form = PhoneForm()

        context = {'form': form, 'message': success_message,'devices_list': devices}
        return render(request, 'lists/devices_list.html', context)

class NewGroupView(View):
    def get(self, request):
        groups = Group.objects.all()
        form = GroupForm()
        success_message = ''
        context = {'form': form, 'message': success_message,'groups_list': groups}
        return render(request, 'lists/groups_list.html', context)

    def post(self, request):
        groups = Group.objects.all()
        success_message = "Grupo creado"
        form = GroupForm()
        if request.method == 'POST':
            form = GroupForm(request.POST)
            if form.is_valid():
                form.save()
                success_message = '''
                <p style="color:green">
                    Guardado con exito!
                </p>
                '''
                form = GroupForm()

        context = {'form': form, 'message': success_message,'groups_list': groups}
        return render(request, 'lists/groups_list.html', context)

class NewOrderView(View):
    def get(self, request):
        orders = Order.objects.all()
        form = OrderForm()
        success_message = ''
        context = {'form': form, 'message': success_message,'orders_list': orders}
        return render(request, 'lists/orders_list.html', context)

    def post(self, request):
        orders = Order.objects.all()
        success_message = "Listado creado"
        form = OrderForm()
        if request.method == 'POST':
            form = OrderForm(request.POST)
            if form.is_valid():
                new_user = form.save()
                success_message = '''
                <p style="color:green">
                    Guardado con exito!
                </p>
                '''
                form = OrderForm()

        context = {'form': form, 'message': success_message,'orders_list': orders}
        return render(request, 'lists/orders_list.html', context)

class NewProductView(View):
    def get(self, request):
        products = Product.objects.all()
        form = ProductForm()
        success_message = ''
        context = {'form': form, 'message': success_message,'products_list': products}
        return render(request, 'lists/products_list.html', context)

    def post(self, request):
        products = Product.objects.all()
        success_message = "Listado creado"
        form = ProductForm()
        if request.method == 'POST':
            form = ProductForm(request.POST)
            if form.is_valid():
                new_user = form.save()
                success_message = '''
                <p style="color:green">
                    Guardado con exito!
                </p>
                '''
                form = ProductForm()

        context = {'form': form, 'message': success_message,'products_list': products}
        return render(request, 'lists/products_list.html', context)


def items_list_view(request):
    items = Item.objects.all()
    context = {'items_list': items}
    return render(request, 'lists/items_list.html', context)


"""
DETAILS
"""

#Details
def user_detail_view(request, pk):
    user = User.objects.filter(pk=pk)[0]
    if request.method == "POST":
        form = UserForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
    else:
        form = UserForm(instance=user)
    return render(request, 'details/user_detail.html', {'form': form, 'user_detail':user})

def group_detail_view(request, pk):
    group = Group.objects.filter(pk=pk)[0]
    if request.method == "POST":
        form = GroupForm(request.POST, instance=group)
        if form.is_valid():
            form.save()
    else:
        form = GroupForm(instance=group)
    return render(request, 'details/group_detail.html', {'form': form, 'group_detail':group})

def device_detail_view(request, pk):
    device = Phone.objects.filter(pk=pk)[0]
    users = device.users()
    if request.method == "POST":
        form = PhoneForm(request.POST, instance=device)
        if form.is_valid():
            form.save()
    else:
        form = PhoneForm(instance=device)
    return render(request, 'details/device_detail.html', {'form': form, 'device_detail':device, 'users':users})

def order_detail_view(request, pk):
    order = Order.objects.filter(pk=pk)[0]
    if request.method == "POST":
        form = OrderForm(request.POST, instance=order)
        if form.is_valid():
            form.save()
    else:
        form = OrderForm(instance=order)
    return render(request, 'details/order_detail.html', {'form': form, 'order_detail':order})

def product_detail_view(request, pk):
    product = Product.objects.filter(pk=pk)[0]
    num_orders = product.item_set.all().count()
    ##hay que recorrer todos los grupos, para saber a cuales pertenece.
    #groups = Product.objects.filter(pk=pk)[0]
    if request.method == "POST":
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
    else:
        form = ProductForm(instance=product)
    context = {'form': form, 'product_detail':product, 'num_orders':num_orders}
    return render(request, 'details/product_detail.html', context)

"""
Deletes
"""
def user_delete_view(request, pk):
    user = User.objects.filter(pk=pk)[0]
    user.delete()
    users = User.objects.all()
    form = UserForm()
    success_message = 'Usuario borrado'
    context = {'form': form, 'message': success_message,'users_list': users}
    return render(request, 'lists/users_list.html', context)

def group_delete_view(request, pk):
    group = Group.objects.filter(pk=pk)[0]
    group.delete()
    groups = User.objects.all()
    form = GroupForm()
    success_message = 'Grupo borrado'
    context = {'form': form, 'message': success_message,'groups_list': groups}
    return render(request, 'lists/groups_list.html', context)

def device_delete_view(request, pk):
    device = Phone.objects.filter(pk=pk)[0]
    device.delete()
    devices = Phone.objects.all()
    form = PhoneForm()
    success_message = 'Usuario borrado'
    context = {'form': form, 'message': success_message,'devices_list': devices}
    return render(request, 'lists/devices_list.html', context)

def product_delete_view(request, pk):
    product = Product.objects.filter(pk=pk)[0]
    product.delete()
    products = Product.objects.all()
    form = ProductForm()
    success_message = 'Producto borrado'
    context = {'form': form, 'message': success_message,'products_list': products}
    return render(request, 'lists/products_list.html', context)

def order_delete_view(request, pk):
    order = Order.objects.filter(pk=pk)[0]
    order.delete()
    orders = Order.objects.all()
    form = OrderForm()
    success_message = 'Listado borrado'
    context = {'form': form, 'message': success_message,'orders_list': orders}
    return render(request, 'lists/orders_list.html', context)



