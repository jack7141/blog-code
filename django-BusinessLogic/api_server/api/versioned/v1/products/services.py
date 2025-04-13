# products/services.py (Services Layer 패턴)
from django.utils import timezone
from django.core.exceptions import ValidationError
from decimal import Decimal

from products.models import Product, DiscountCode


class DiscountService:
    @staticmethod
    def validate_discount_code(discount_code_str):
        """할인 코드 유효성 검증"""
        try:
            discount = DiscountCode.objects.get(code=discount_code_str, is_active=True)

            if discount.expires_at and timezone.now() > discount.expires_at:
                raise ValidationError("할인 코드가 만료되었습니다.")

            return discount

        except DiscountCode.DoesNotExist:
            raise ValidationError("유효하지 않은 할인 코드입니다.")

    @staticmethod
    def calculate_discount(product, discount_percentage):
        """제품 할인 계산"""
        discount_amount = product.price * (discount_percentage / Decimal('100'))
        return product.price - discount_amount

    @staticmethod
    def get_discounted_products(discount_code_str):
        """모든 제품에 할인 적용"""
        # 할인 코드 유효성 검증
        discount = DiscountService.validate_discount_code(discount_code_str)

        # 모든 제품에 할인 적용
        products = Product.objects.all()
        result = []

        for product in products:
            discounted_price = DiscountService.calculate_discount(
                product, discount.percentage
            )

            result.append({
                'id': product.id,
                'name': product.name,
                'original_price': product.price,
                'discounted_price': discounted_price
            })

        return result