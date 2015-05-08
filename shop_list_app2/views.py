from django.shortcuts import render

from models import User, Group,Product, Order, Phone

# Create your views here.

def dashboard(request):
    db_user_list = User.objects.all()
    db_group_list = Group.objects.all()
    context = {'user_list': db_user_list,
               'group_list': db_group_list}
    return render(request, 'dashboard.html',context)

def group_list(request):
    group_list = Group.objects.all()
    context = {'group_list': group_list}
    return render(request, 'group_list.html',context)

def group_detail(request, pk):
    '''
    Presenta el detalle de una imagen
    '''
    group = Group.objects.filter(pk=pk)
    selected_group = group[0]

    context = { 'group_detail' : selected_group }
    return render(request, 'group_detail.html', context)