__author__ = 'rubenvos'
# -*- coding: utf-8 -*-

from django.forms import ModelForm
from models import User, Group, Phone, Product, Order


class UserForm(ModelForm):

    class Meta:
        model = User
        fields = ['name', 'last_name','email','active','device','friends'] #Como chequear campos obligatorios

class GroupForm(ModelForm):

    class Meta:
        model = Group
        fields = ['name', 'active','avatar','users','orders'] #Como chequear campos obligatorios

class PhoneForm(ModelForm):

    class Meta:
        model = Phone
        fields = ['id_device', 'active','os'] #Como chequear campos obligatorios

class OrderForm(ModelForm):

    class Meta:
        model = Order
        fields = ['name', 'active'] #Como chequear campos obligatorios

class ProductForm(ModelForm):

    class Meta:
        model = Product
        fields = ['name','active','avatar','quantity','measure'] #Como chequear campos obligatorios