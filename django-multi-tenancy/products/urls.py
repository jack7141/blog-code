from django.urls import path
from .views import ProductListView, ProductDetailView, TenantInfoView

app_name = 'products'

urlpatterns = [
    path('api/products/', ProductListView.as_view(), name='product-list'),
    path('api/products/<int:product_id>/', ProductDetailView.as_view(), name='product-detail'),
    path('api/tenant-info/', TenantInfoView.as_view(), name='tenant-info'),
]