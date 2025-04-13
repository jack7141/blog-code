from drf_spectacular.utils import extend_schema, OpenApiParameter
from rest_framework import viewsets
from rest_framework.serializers import Serializer
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST
from rest_framework.exceptions import ValidationError

from api_server.api.versioned.v1.products.serializers import ProductSerializer, DiscountedProductSerializer
from api_server.api.versioned.v1.products.services import DiscountService
from products.models import Product


class ProductsViewSet(viewsets.ReadOnlyModelViewSet):
    permission_classes = [AllowAny, ]
    serializer_class = ProductSerializer
    queryset = Product.objects.all()

    @extend_schema(
        parameters=[
            OpenApiParameter(name='discount_code', description='할인 코드', required=True, type=str)
        ]
    )
    def fatmodel(self, request, *args, **kwargs):
        discount_code = request.query_params.get('discount_code')
        try:
            # 모델 메서드 호출
            discounted_products = Product.get_discounted_products(discount_code)
            return Response(discounted_products, status=HTTP_200_OK)

        except ValidationError as e:
            return Response({"error": str(e)}, status=HTTP_400_BAD_REQUEST)

    @extend_schema(
        parameters=[
            OpenApiParameter(name='discount_code', description='할인 코드', required=True, type=str)
        ]
    )
    def serializer_pattern(self, request, *args, **kwargs):
        """Serializer 패턴을 사용한 할인 로직"""
        discount_code = request.query_params.get('discount_code')

        if not discount_code:
            return Response(
                {"error": "할인 코드를 제공해주세요."},
                status=HTTP_400_BAD_REQUEST
            )

        from rest_framework import serializers
        try:
            products = self.get_queryset()
            serializer = DiscountedProductSerializer(
                products,
                many=True,
                context={'discount_code': discount_code}
            )
            return Response(serializer.data, status=HTTP_200_OK)

        except serializers.ValidationError as e:
            return Response({"error": str(e)}, status=HTTP_400_BAD_REQUEST)

    @extend_schema(
        parameters=[
            OpenApiParameter(name='discount_code', description='할인 코드', required=True, type=str)
        ]
    )
    def service_pattern(self, request, *args, **kwargs):
        """Service Layer 패턴을 사용한 할인 로직"""
        discount_code = request.query_params.get('discount_code')

        if not discount_code:
            return Response(
                {"error": "할인 코드를 제공해주세요."},
                status=HTTP_400_BAD_REQUEST
            )

        try:
            # 서비스 레이어 호출
            discounted_products = DiscountService.get_discounted_products(discount_code)
            return Response(discounted_products, status=HTTP_200_OK)

        except ValidationError as e:
            return Response({"error": str(e)}, status=HTTP_400_BAD_REQUEST)

    @extend_schema(
        parameters=[
            OpenApiParameter(name='discount_code', description='할인 코드', required=True, type=str)
        ]
    )
    def queryset_pattern(self, request, *args, **kwargs):
        """QuerySet + Manager 패턴을 사용한 할인 로직"""
        discount_code = request.query_params.get('discount_code')

        if not discount_code:
            return Response(
                {"error": "할인 코드를 제공해주세요."},
                status=HTTP_400_BAD_REQUEST
            )

        try:
            # Manager 메서드 호출
            products_with_discount = Product.objects.with_discount(discount_code)

            # 직접 응답 형식 구성
            result = [{
                'id': product.id,
                'name': product.name,
                'original_price': product.price,
                'discounted_price': product.discounted_price
            } for product in products_with_discount]

            return Response(result, status=HTTP_200_OK)

        except ValidationError as e:
            return Response({"error": str(e)}, status=HTTP_400_BAD_REQUEST)