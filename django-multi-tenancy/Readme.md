# Django Multi-Tenancy

SaaS(Software as a Service) 서비스에서 기업별 데이터를 안전하게 분리하기 위한 Django 프로젝트입니다. PostgreSQL 스키마를 활용한 다중 테넌트 아키텍처를 구현합니다.

## 개요

이 프로젝트는 django-tenants 라이브러리를 사용하여 다중 테넌트 환경을 구현하는 방법을 보여줍니다. 각 테넌트(기업)는 완전히 분리된 데이터베이스 스키마를 갖게 되어, 데이터 격리와 보안을 보장합니다.

## 설치 방법

1. 필수 패키지 설치
```bash
pip install -r requirements.txt
```

2. PostgreSQL 설정 (반드시 PostgreSQL을 사용해야 합니다)
```bash
# 적절한 데이터베이스 생성
createdb multitenancy_db
```

3. 환경 설정 및 마이그레이션
```bash
# 마이그레이션 실행
python manage.py migrate_schemas --shared
```

## 프로젝트 구조

```
django-multi-tenancy/
├── configs/            # 프로젝트 설정
├── customers/          # 테넌트 정보 관리 앱
├── products/           # 테넌트별 상품 관리 앱
├── order/              # 테넌트별 주문 관리 앱
└── store/              # 테넌트별 매장 관리 앱
```

## 테넌트 관리

### 테넌트 생성

```python
from customers.models import Client, Domain

# 새 테넌트 생성
tenant = Client(
    schema_name='tenant1',  # 스키마 이름
    name='First Client',    # 테넌트 이름
    paid_until='2025-12-31',
    on_trial=True
)
tenant.save()

# 테넌트 도메인 설정
domain = Domain()
domain.domain = 'tenant1.localhost'  # 로컬 개발용
domain.tenant = tenant
domain.is_primary = True
domain.save()
```

### 테넌트 데이터 액세스

```python
from django_tenants.utils import tenant_context
from customers.models import Client
from products.models import Product

# 테넌트 불러오기
tenant = Client.objects.get(schema_name='tenant1')

# 특정 테넌트 컨텍스트에서 작업
with tenant_context(tenant):
    # 상품 생성
    Product.objects.create(
        name="테넌트1 상품", 
        description="테넌트1 전용 상품", 
        price=15000
    )
    
    # 상품 조회
    products = Product.objects.all()
    print(f"테넌트1 상품 개수: {products.count()}")
```

## 마이그레이션 관리

django-tenants에서는 다양한 마이그레이션 옵션을 제공합니다:

```bash
# 공유 앱만 마이그레이션 (public 스키마)
python manage.py migrate_schemas --shared

# 테넌트 앱만 마이그레이션 (각 테넌트 스키마)
python manage.py migrate_schemas --tenant

# 모든 앱 마이그레이션 (공유 + 테넌트)
python manage.py migrate_schemas
```

공유 앱과 테넌트 앱이 다른 이유는 데이터를 논리적으로 분리하기 위함입니다:

- `customers` 앱은 공유 스키마에만 있어야 테넌트 정보를 한 곳에서 관리할 수 있습니다.
- `products` 앱은 각 테넌트 스키마에 있어야 테넌트별로 다른 상품 정보를 가질 수 있습니다.

이 설계로 인해 django-tenants는 어떤 마이그레이션을 어느 스키마에 적용할지 구분해야 합니다.

> **참고**: 만약 모든 앱이 모든 스키마에 존재해야 한다면, `SHARED_APPS`와 `TENANT_APPS` 목록을 적절히 조정해야 합니다.

## 설정 가이드

### settings.py 주요 설정

```python
INSTALLED_APPS = [
    'django_tenants',  # 가장 먼저 로드되어야 함
    'customers',       # 테넌트 모델이 있는 앱
    # 나머지 앱들...
]

SHARED_APPS = [
    'django_tenants',
    'customers',
    # 공유 앱들...
]

TENANT_APPS = [
    'products',
    'order',
    'store',
    # 테넌트별 앱들...
]

MIDDLEWARE = [
    'django_tenants.middleware.main.TenantMainMiddleware',  # 가장 먼저 로드
    # 나머지 미들웨어...
]

DATABASES = {
    'default': {
        'ENGINE': 'django_tenants.postgresql_backend',  # 특수 백엔드 사용
        # 데이터베이스 설정...
    }
}

TENANT_MODEL = "customers.Client"  # 테넌트 모델
TENANT_DOMAIN_MODEL = "customers.Domain"  # 도메인 모델
```

## API 엔드포인트

- `/api/tenant-info/` - 현재 테넌트 정보 확인
- `/api/products/` - 현재 테넌트의 상품 목록
- `/api/products/<id>/` - 특정 상품 상세 정보

## 주의사항

1. **PostgreSQL 필수**: django-tenants는 PostgreSQL의 스키마 기능에 의존합니다.
2. **마이그레이션 주의**: 테넌트가 많을수록 마이그레이션 시간이 길어집니다.
3. **도메인 설정**: 각 테넌트는 고유한 도메인이나 서브도메인이 필요합니다.
