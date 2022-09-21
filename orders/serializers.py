from rest_framework import serializers
from accounts.models import Profile
from accounts.serializers import ProfileSerializer
from .models import *

from products.serializers import ProductSerializer

class MyOrderItemSerializer(serializers.ModelSerializer):    
    product = ProductSerializer()

    class Meta:
        model = OrderItem
        fields = (
            "product",
            "quantity",
        )

class MyOrderSerializer(serializers.ModelSerializer):
    items = MyOrderItemSerializer(many=True)
    user = ProfileSerializer(many=False)
    class Meta:
        model = Order
        fields = (
            "id",
            "user",
            "items",
            "paid_amount"
        )

class OrderItemSerializer(serializers.ModelSerializer):    
    class Meta:
        model = OrderItem
        product = ProductSerializer(many=False)
        fields = (
            "product",
            "quantity",
        )

class OrderSerializer(serializers.ModelSerializer):
    items = OrderItemSerializer(many=True)
    user = ProfileSerializer(many=False, read_only=True)
    class Meta:
        model = Order
        fields = (
            "id",
            "user",
            "paid_amount",
            "items"
            
        )
        extra_kwargs = {'user': {'required': False}}
    
    def create(self, validated_data):
        items_data = validated_data.pop('items')
        order = Order.objects.create(**validated_data)

        for item_data in items_data:
            OrderItem.objects.create(order=order, **item_data)
            
        return order