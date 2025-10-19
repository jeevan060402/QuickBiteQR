from rest_framework import serializers
from .models import MenuCategory, MenuItem, Order, OrderItem


class MenuItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = MenuItem
        fields = ('id', 'name', 'description', 'price', 'available')


class MenuCategorySerializer(serializers.ModelSerializer):
    items = MenuItemSerializer(many=True)

    class Meta:
        model = MenuCategory
        fields = ('id', 'name', 'items')


class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = ('menu_item', 'quantity', 'price')


class OrderSerializer(serializers.ModelSerializer):
    items = OrderItemSerializer(many=True)

    class Meta:
        model = Order
        fields = ('id', 'restaurant', 'table', 'total', 'status', 'items')

    def create(self, validated_data):
        items = validated_data.pop('items', [])
        order = Order.objects.create(**validated_data)
        total = 0
        for it in items:
            menu = it['menu_item']
            qty = it.get('quantity', 1)
            price = menu.price
            OrderItem.objects.create(order=order, menu_item=menu, quantity=qty, price=price)
            total += price * qty
        order.total = total
        order.save()
        return order
