from django.urls import path
from .views import ProductsViewSet

urlpatterns = [
    path('fatmodel/', ProductsViewSet.as_view({'get': 'fatmodel'})),
    path('serializer-pattern/', ProductsViewSet.as_view({'get': 'serializer_pattern'})),
    path('service-pattern/', ProductsViewSet.as_view({'get': 'service_pattern'})),
    path('queryset-pattern/', ProductsViewSet.as_view({'get': 'queryset_pattern'}))
]
