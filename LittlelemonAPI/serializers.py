from rest_framework import serializers
from django.contrib.auth.models import User, Group
from . import models

class GroupSerializer(serializers.ModelSerializer):    
    class Meta:
        model = Group
        fields = ['name',]

class UserSerializer(serializers.ModelSerializer):
    groups = GroupSerializer(read_only=True, many=True)
    class Meta:
        model = User
        fields = ['username', 'id', 'email', 'groups',]
        # fields = '__all__'
        # depth = 1


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Category
        fields = ['id', 'slug', 'title']
        
class MenuItemSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)
    category_id = serializers.IntegerField(write_only=True)
    class Meta:
        model = models.MenuItem
        fields = ['id', 'title', 'price', 'featured', 'category', 'category_id']
        depth = 1


class CartSerializer(serializers.ModelSerializer):
    # price = serializers.SerializerMethodField(method_name = 'calculate_price')
    # unit_price = serializers.SerializerMethodField(method_name = 'menuitem_price')
    menuitem = MenuItemSerializer(read_only=True)
    menuitem_id = serializers.IntegerField(write_only=True)
    user = UserSerializer(read_only=True)
    user_id = serializers.IntegerField(write_only=True)
    class Meta:
        model = models.Cart
        fields = ['user', 'user_id', 'menuitem', 'menuitem_id', 'quantity', 'unit_price', 'price']


class OrderItemSerializer(serializers.ModelSerializer):
    # order = UserSerializer(read_only=True)
    user_id = serializers.IntegerField()
    menuitem = MenuItemSerializer(read_only=True)
    menuitem_id = serializers.IntegerField(write_only=True)
    class Meta:
        model = models.OrderItem
        fields = ['user_id', 'menuitem', 'menuitem_id', 'quantity', 'unit_price', 'price']

class OrderSerializer(serializers.ModelSerializer):
    # user = UserSerializer(read_only=True)
    user_id = serializers.IntegerField(write_only=True)
    orderitem = OrderItemSerializer(read_only=True)
    orderitem_id = serializers.IntegerField(write_only=True)
    
    class Meta:
        model = models.Order
        fields = ['id', 'user_id', 'delivery_crew','status', 'total', 'date', 'orderitem', 'orderitem_id',]