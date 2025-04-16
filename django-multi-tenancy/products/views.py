from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Product
from .serializers import ProductSerializer


class ProductListView(APIView):
    def get(self, request):
        # 현재 테넌트 정보 가져오기
        current_tenant = request.tenant

        # 현재 테넌트의 제품 목록 조회
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)

        return Response({
            'tenant': {
                'name': current_tenant.name,
                'schema_name': current_tenant.schema_name
            },
            'products': serializer.data
        })