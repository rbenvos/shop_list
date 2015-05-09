# -*- coding: utf-8 -*-

from django.shortcuts import render
from models import User, Group,Product, Order, Phone
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
    db_products_list = Product.objects.all().order_by("-created_at")[:5]
    context = {'db_users_list': db_users_list,
               'db_groups_list': db_groups_list,
               'db_devices_list': db_devices_list,
               'db_orders_list': db_orders_list,
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
        success_message = "Usuario creado"
        form = UserForm()
        if request.method == 'POST':
            form = UserForm(request.POST)
            if form.is_valid():
                new_user = form.save()
                success_message = '''
                <p style="color:green">
                    Guardado con exito!
                </p>
                '''
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
                new_user = form.save()
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
                new_user = form.save()
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

"""
DETAILS
"""

#Details
def user_detail_view(request, pk):
    user = User.objects.filter(pk=pk)[0]
    context = { 'user_detail' : user }
    return render(request, 'details/user_detail.html', context)

def group_detail_view(request, pk):
    group = Group.objects.filter(pk=pk)
    selected_group = group[0]
    context = { 'group_detail' : selected_group }
    return render(request, 'details/group_detail.html', context)

def device_detail_view(request, pk):
    device = Phone.objects.filter(pk=pk)[0]
    users = device.users()
    context = { 'device_detail' : device,
                'users': users}
    return render(request, 'details/device_detail.html', context)

def order_detail_view(request, pk):
    order = Order.objects.filter(pk=pk)[0]
    context = { 'order_detail' : order }
    return render(request, 'details/order_detail.html', context)

def product_detail_view(request, pk):
    product = Product.objects.filter(pk=pk)[0]
    context = { 'product_detail' : product }
    return render(request, 'details/product_detail.html', context)

