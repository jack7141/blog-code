from rest_framework import viewsets
from rest_framework.serializers import Serializer
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework.status import HTTP_200_OK

from api_server.api.versioned.v1.products.serializers import ProductSerializer
from products.models import Product


class ProductsViewSet(viewsets.ReadOnlyModelViewSet):
    permission_classes = [AllowAny, ]
    serializer_class = ProductSerializer
    queryset = Product.objects.all()

    def fatmodel(self, request, *args, **kwargs):
        return Response(status=HTTP_200_OK)