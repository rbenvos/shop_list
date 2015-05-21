# -*- coding: utf-8 -*-
from rest_framework import serializers
from shop_list_app2.models import User, Product, Group, Order, Phone, Item

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User

class UserSimpleSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        field = ['id','name','last_name','email','active']

class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group

class PhoneSerializer(serializers.ModelSerializer):
    class Meta:
        model = Phone

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order

class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
