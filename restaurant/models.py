import uuid
from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Restaurant(models.Model):
    owner = models.OneToOneField(User, on_delete=models.CASCADE, related_name='restaurant')
    name = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name


class Table(models.Model):
    STATUS_CHOICES = [('ready', 'Ready'), ('busy', 'Busy'), ('offline', 'Offline')]
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE, related_name='tables')
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    table_number = models.PositiveIntegerField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='ready')

    class Meta:
        unique_together = ('restaurant', 'table_number')

    def __str__(self):
        return f"{self.restaurant.name} - {self.table_number}"


class MenuCategory(models.Model):
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE, related_name='categories')
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class MenuItem(models.Model):
    category = models.ForeignKey(MenuCategory, on_delete=models.CASCADE, related_name='items')
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    available = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class Order(models.Model):
    STATUS_CHOICES = [('pending', 'Pending'), ('preparing', 'Preparing'), ('served', 'Served'), ('cancelled', 'Cancelled')]
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE, related_name='orders')
    table = models.ForeignKey(Table, on_delete=models.SET_NULL, null=True, blank=True, related_name='orders')
    total = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Order {self.id} - {self.restaurant.name}"


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items')
    menu_item = models.ForeignKey(MenuItem, on_delete=models.PROTECT)
    quantity = models.PositiveIntegerField(default=1)
    price = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        return f"{self.quantity}x {self.menu_item.name}"
