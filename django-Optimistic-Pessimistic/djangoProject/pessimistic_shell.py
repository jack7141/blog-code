from django.db import transaction
from pessimistic.models import Product

def update_product_stock(product_id, quantity):
    with transaction.atomic():
        # SQL문 예시: SELECT ... FOR UPDATE 구문으로 해당 레코드에 잠금 획득
        product = Product.objects.select_for_update().get(id=product_id)

        # Lock을 걸어두고 product에 접근
        if product.stock >= quantity:
            product.stock -= quantity
            product.save()
            return True
        else:
            # 재고 부족
            return False