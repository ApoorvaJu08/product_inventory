from rest_framework import generics
from .models import Supplier, Product
from .serializers import SupplierSerializer, ProductSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404


class SupplierListCreate(generics.ListCreateAPIView):
    queryset = Supplier.objects.all()
    serializer_class = SupplierSerializer


class ProductListCreate(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductList(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_fields = ['supplier', 'price']
    ordering_fields = ['price']


class ProductRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductUpdate(generics.UpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def get_object(self):
        pk = self.kwargs.get('pk')
        return get_object_or_404(Product, pk=pk)
    

class ProductDelete(generics.DestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def get_object(self):
        pk = self.kwargs.get('pk')
        return get_object_or_404(Product, pk=pk)
    

class AdjustStock(APIView):
    def patch(self, request, pk):
        product = get_object_or_404(Product, pk=pk)
        operation = request.data.get('operation')
        quantity = request.data.get('quantity')
        
        if operation == 'increment':
            product.stock_quantity += quantity
        elif operation == 'decrement':
            product.stock_quantity -= quantity
            if product.stock_quantity < 0:
                return Response({"error": "Stock cannot be negative"}, status=status.HTTP_400_BAD_REQUEST)
        
        product.save()
        serializer = ProductSerializer(product)
        return Response(serializer.data)
