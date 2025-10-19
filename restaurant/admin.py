from django.contrib import admin
from .models import Restaurant, Table, MenuCategory, MenuItem, Order, OrderItem


@admin.register(Restaurant)
class RestaurantAdmin(admin.ModelAdmin):
    list_display = ('name', 'owner')


@admin.register(Table)
class TableAdmin(admin.ModelAdmin):
    list_display = ('restaurant', 'table_number', 'status', 'uuid')
    readonly_fields = ('uuid',)


@admin.register(MenuCategory)
class MenuCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'restaurant')


@admin.register(MenuItem)
class MenuItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'price', 'available')


class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 0


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'restaurant', 'table', 'total', 'status', 'created_at')
    inlines = [OrderItemInline]
