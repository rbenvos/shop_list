# -*- coding: utf-8 -*-
from rest_framework import serializers
from models import User, Product

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
