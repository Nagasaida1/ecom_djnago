from django.urls import path
from .views import ProductListView, ProductCreateView, ProductUpdateView, ProductDeleteView, OrderHistoryView

urlpatterns = [
    path('products/', ProductListView.as_view(), name='product-list'),
    path('products/create/', ProductCreateView.as_view(), name='product-create'),
    path('products/update/<int:pk>/', ProductUpdateView.as_view(), name='product-update'),
    path('products/delete/<int:pk>/', ProductDeleteView.as_view(), name='product-delete'),
    path('orders/', OrderHistoryView.as_view(), name='order-history'),
]
