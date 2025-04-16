from django_tenants.utils import tenant_context
from customers.models import Client
from products.models import Product

# 테넌트 불러오기
public_tenant = Client.objects.get(schema_name='tenant1')
tenant2 = Client.objects.get(schema_name='tenant2')

# 공용 테넌트에 상품 추가
with tenant_context(public_tenant):
    Product.objects.create(
        name="테넌트1 상품 1",
        description="테넌트1 전용 상품",
        price=10000
    )
    Product.objects.create(
        name="테넌트1 상품 2",
        description="테넌트1 전용 상품",
        price=20000
    )

    # 데이터 생성 확인
    print(f"테넌트1 상품 개수: {Product.objects.count()}")

with tenant_context(tenant2):
    Product.objects.create(
        name="테넌트2 상품 1",
        description="테넌트2 전용 상품",
        price=15000
    )
    Product.objects.create(
        name="테넌트2 상품 2",
        description="테넌트2의 프리미엄 상품",
        price=30000
    )
    Product.objects.create(
        name="테넌트2 상품 3",
        description="테넌트2 한정판",
        price=50000
    )

    # 데이터 생성 확인
    print(f"테넌트2 상품 개수: {Product.objects.count()}")
