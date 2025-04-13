from rest_framework import serializers

from products.models import Product, DiscountCode


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class DiscountedProductSerializer(serializers.ModelSerializer):
    original_price = serializers.DecimalField(max_digits=10, decimal_places=2, read_only=True)
    discounted_price = serializers.DecimalField(max_digits=10, decimal_places=2, read_only=True)

    class Meta:
        model = Product
        fields = ['id', 'name', 'original_price', 'discounted_price']

    def to_representation(self, instance):
        """직렬화 중 할인 적용"""
        data = super().to_representation(instance)

        # context에서 할인 코드 가져오기
        discount_code_str = self.context.get('discount_code')

        if not discount_code_str:
            return data

        try:
            # 할인 코드 유효성 검증
            discount = DiscountCode.objects.get(code=discount_code_str, is_active=True)

            from django.utils import timezone
            if discount.expires_at and timezone.now() > discount.expires_at:
                raise serializers.ValidationError("할인 코드가 만료되었습니다.")

            # 할인 계산
            original_price = instance.price
            discount_amount = original_price * (discount.percentage / Decimal('100'))
            discounted_price = original_price - discount_amount

            # 결과 업데이트
            data['original_price'] = str(original_price)
            data['discounted_price'] = str(discounted_price)

            return data

        except DiscountCode.DoesNotExist:
            raise serializers.ValidationError("유효하지 않은 할인 코드입니다.")