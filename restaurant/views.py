from rest_framework import generics, status
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from .models import MenuCategory, MenuItem, Order, Table, Restaurant
from .serializers import MenuCategorySerializer, OrderSerializer


class MenuListView(generics.ListAPIView):
    queryset = MenuCategory.objects.prefetch_related('items').all()
    serializer_class = MenuCategorySerializer


class CreateOrderView(generics.CreateAPIView):
    serializer_class = OrderSerializer

    def create(self, request, *args, **kwargs):
        table_uuid = request.data.get('table_uuid')
        if table_uuid:
            try:
                table = Table.objects.get(uuid=table_uuid)
                if table.status != 'ready':
                    return Response({'detail': 'table not ready'}, status=status.HTTP_400_BAD_REQUEST)
                request.data['table'] = table.id
                request.data['restaurant'] = table.restaurant.id
            except Table.DoesNotExist:
                return Response({'detail': 'invalid table'}, status=status.HTTP_400_BAD_REQUEST)
        return super().create(request, *args, **kwargs)
