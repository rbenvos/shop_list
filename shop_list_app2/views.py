from django.shortcuts import render

from models import User, Group,Product, Order, Phone

# Dashboard

def dashboard(request):
    db_users_list = User.objects.all()[:5]
    db_groups_list = Group.objects.all()[:5]
    db_devices_list = Phone.objects.all()[:5]
    db_orders_list = Order.objects.all()[:5]
    db_products_list = Product.objects.all()[:5]
    context = {'db_users_list': db_users_list,
               'db_groups_list': db_groups_list,
               'db_devices_list': db_devices_list,
               'db_orders_list': db_orders_list,
               'db_products_list': db_products_list,
               }
    return render(request, 'dashboard.html',context)


#Main
def groups_list_view(request):
    groups_list = Group.objects.all()
    context = {'groups_list': groups_list}
    return render(request, 'groups_list.html',context)

def users_list_view(request):
    users_list = User.objects.all()
    context = {'users_list': users_list}
    return render(request, 'users_list.html',context)

def devices_list_view(request):
    devices_list = Phone.objects.all()
    context = {'devices_list': devices_list}
    return render(request, 'devices_list.html',context)

def orders_list_view(request):
    orders_list = Order.objects.all()
    context = {'orders_list': orders_list}
    return render(request, 'orders_list.html',context)

def products_list_view(request):
    products_list = Product.objects.all()
    context = {'products_list': products_list}
    return render(request, 'products_list.html',context)


#Details
def user_detail_view(request, pk):
    '''
    Presenta el detalle de una imagen
    '''
    user = User.objects.filter(pk=pk)[0]
    context = { 'user_detail' : user }
    return render(request, 'user_detail.html', context)

def group_detail_view(request, pk):
    '''
    Presenta el detalle de una imagen
    '''
    group = Group.objects.filter(pk=pk)
    selected_group = group[0]

    context = { 'group_detail' : selected_group }
    return render(request, 'group_detail.html', context)

def device_detail_view(request, pk):
    '''
    Presenta el detalle de una imagen
    '''
    device = Phone.objects.filter(pk=pk)[0]
    context = { 'device_detail' : device }
    return render(request, 'device_detail.html', context)

def order_detail_view(request, pk):
    '''
    Presenta el detalle de una imagen
    '''
    order = Order.objects.filter(pk=pk)[0]
    context = { 'order_detail' : order }
    return render(request, 'order_detail.html', context)

def product_detail_view(request, pk):
    '''
    Presenta el detalle de una imagen
    '''
    product = Product.objects.filter(pk=pk)[0]
    context = { 'product_detail' : product }
    return render(request, 'product_detail.html', context)