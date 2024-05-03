from django.urls import path
from .views import ProductListCreate, ProductUpdate, ProductDelete, AdjustStock, SupplierListCreate


urlpatterns = [
    path('products/create/', ProductListCreate.as_view(), name='product-create'),
    path('products/<int:pk>/update/', ProductUpdate.as_view(), name='product-update'),
    path('products/<int:pk>/delete/', ProductDelete.as_view(), name='product-delete'),
    path('products/<int:pk>/adjust-stock/', AdjustStock.as_view(), name='adjust-stock'),
    path('suppliers/', SupplierListCreate.as_view(), name='supplier-list-create'),
]
