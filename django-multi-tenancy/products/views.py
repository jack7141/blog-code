from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Product
from .serializers import ProductSerializer
from django_tenants.utils import get_tenant_model


class ProductListView(APIView):
    """
    테넌트별 제품 목록을 반환하는 API View
    """

    def get(self, request):
        # 현재 테넌트 정보 가져오기
        current_tenant = request.tenant

        # 현재 테넌트의 제품 목록 조회
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)

        # 테넌트 정보와 함께 응답
        return Response({
            'tenant': {
                'name': current_tenant.name,
                'schema_name': current_tenant.schema_name
            },
            'products': serializer.data
        })


class ProductDetailView(APIView):
    """
    단일 제품 정보를 반환하는 API View
    """

    def get(self, request, product_id):
        try:
            product = Product.objects.get(pk=product_id)
            serializer = ProductSerializer(product)
            return Response(serializer.data)
        except Product.DoesNotExist:
            return Response(
                {'error': '제품을 찾을 수 없습니다'},
                status=status.HTTP_404_NOT_FOUND
            )


class TenantInfoView(APIView):
    """
    현재 테넌트 정보를 반환하는 API View
    """

    def get(self, request):
        current_tenant = request.tenant
        return Response({
            'tenant_name': current_tenant.name,
            'schema_name': current_tenant.schema_name,
            'product_count': Product.objects.count(),
            'domain': request.get_host()
        })