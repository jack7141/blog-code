from django.db import transaction
from django.db.models import F

from optimistic.models import Product


class OptimisticLockException(Exception):
    pass


# update_product 함수 정의
def update_product(product_id, user_data, current_version):
    try:
        with transaction.atomic():
            # 버전을 조건으로 업데이트 시도
            rows_updated = Product.objects.filter(
                id=product_id,
                version=current_version
            ).update(
                name=user_data['name'],
                price=user_data['price'],
                stock=user_data['stock'],
                version=F('version') + 1  # 버전 증가
            )
            if rows_updated == 0:
                # 업데이트된 행이 없으면 충돌이 발생했다는 의미
                raise OptimisticLockException("다른 사용자가 이미 데이터를 수정했습니다.")

            return Product.objects.get(id=product_id)
    except OptimisticLockException as e:
        # 충돌 발생 시 처리 로직
        # 예: 최신 데이터 가져와서 사용자에게 재시도 유도
        latest_product = Product.objects.get(id=product_id)
        print(f"충돌 발생: {e}")
        print(f"최신 버전: {latest_product.version}")
        return latest_product

# 테스트용 제품 생성
product = Product.objects.create(name="테스트 상품", price=10000, stock=100)

# 정상 케이스 테스트
user_data = {
    'name': '업데이트된 상품',
    'price': 12000,
    'stock': 90
}
result = update_product(product.id, user_data, product.version)
print(f"업데이트 성공: {result.name}, 가격: {result.price}, 재고: {result.stock}, 버전: {result.version}")

# 충돌 케이스 테스트 (다른 사용자가 이미 수정한 상황 가정)
# 이전 버전을 사용해 업데이트 시도
old_version = 0  # 이전 버전
user_data = {
    'name': '다른 업데이트',
    'price': 15000,
    'stock': 80
}
result = update_product(product.id, user_data, old_version)
print(f"충돌 후 최신 상태: {result.name}, 가격: {result.price}, 재고: {result.stock}, 버전: {result.version}")