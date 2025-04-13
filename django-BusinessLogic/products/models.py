# products/models.py (Fat Model 패턴)
from django.db import models
from django.core.exceptions import ValidationError
from decimal import Decimal
"""
FatModel 방식
"""
class DiscountCode(models.Model):
    code = models.CharField(max_length=20, unique=True)
    percentage = models.DecimalField(max_digits=5, decimal_places=2)
    is_active = models.BooleanField(default=True)
    expires_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.code


class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.name

    def apply_discount(self, discount_code_str):
        """제품에 할인 적용 (Fat Model 패턴)"""
        try:
            discount = DiscountCode.objects.get(code=discount_code_str, is_active=True)

            # 할인 코드 유효성 검증
            if discount.expires_at and timezone.now() > discount.expires_at:
                raise ValidationError("할인 코드가 만료되었습니다.")

            # 할인 계산
            discount_amount = self.price * (discount.percentage / Decimal('100'))
            discounted_price = self.price - discount_amount

            return {
                'product': self,
                'original_price': self.price,
                'discount_code': discount_code_str,
                'discount_percentage': discount.percentage,
                'discounted_price': discounted_price
            }

        except DiscountCode.DoesNotExist:
            raise ValidationError("유효하지 않은 할인 코드입니다.")

    @classmethod
    def get_discounted_products(cls, discount_code_str):
        """모든 제품에 할인 적용 (Fat Model 패턴)"""
        try:
            # 할인 코드 유효성 검증
            discount = DiscountCode.objects.get(code=discount_code_str, is_active=True)
            from django.utils import timezone
            if discount.expires_at and timezone.now() > discount.expires_at:
                raise ValidationError("할인 코드가 만료되었습니다.")

            # 모든 제품에 할인 적용
            products = cls.objects.all()
            result = []

            for product in products:
                discount_amount = product.price * (discount.percentage / Decimal('100'))
                discounted_price = product.price - discount_amount

                result.append({
                    'id': product.id,
                    'name': product.name,
                    'original_price': product.price,
                    'discounted_price': discounted_price
                })

            return result

        except DiscountCode.DoesNotExist:
            raise ValidationError("유효하지 않은 할인 코드입니다.")



"""
Queryset + Manager를 활용한 방식
"""
class DiscountCode(models.Model):
    code = models.CharField(max_length=20, unique=True)
    percentage = models.DecimalField(max_digits=5, decimal_places=2)
    is_active = models.BooleanField(default=True)
    expires_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.code


class ProductQuerySet(models.QuerySet):
    def with_discount(self, discount_code_str):
        """할인이 적용된 제품 쿼리셋 반환"""
        try:
            # 할인 코드 유효성 검증
            discount = DiscountCode.objects.get(code=discount_code_str, is_active=True)

            if discount.expires_at and timezone.now() > discount.expires_at:
                raise ValidationError("할인 코드가 만료되었습니다.")

            # 제품 목록을 가져온 후 각 제품에 할인 적용
            products = list(self)
            result = []

            for product in products:
                discount_amount = product.price * (discount.percentage / Decimal('100'))
                discounted_price = product.price - discount_amount

                # 원본 제품 객체에 속성 추가
                product.discounted_price = discounted_price
                product.discount_percentage = discount.percentage
                result.append(product)

            return result

        except DiscountCode.DoesNotExist:
            raise ValidationError("유효하지 않은 할인 코드입니다.")


class ProductManager(models.Manager):
    def get_queryset(self):
        return ProductQuerySet(self.model, using=self._db)

    def with_discount(self, discount_code_str):
        """할인이 적용된 제품 목록 반환"""
        return self.get_queryset().with_discount(discount_code_str)


class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField(default=0)

    # 기본 매니저 교체
    objects = ProductManager()

    def __str__(self):
        return self.name