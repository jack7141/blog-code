# models.py (Fat Model 접근법)
from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from decimal import Decimal


class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField(default=0)
    is_on_sale = models.BooleanField(default=False)

    def check_stock(self, quantity):
        """재고 확인 메서드"""
        if self.stock < quantity:
            raise ValidationError(f"Not enough stock for {self.name}. Available: {self.stock}")
        return True

    def reduce_stock(self, quantity):
        """재고 차감 메서드"""
        if self.check_stock(quantity):
            self.stock -= quantity
            self.save()

    def __str__(self):
        return self.name


class Order(models.Model):
    STATUS_CHOICES = (
        ('PENDING', 'Pending'),
        ('PAID', 'Paid'),
        ('SHIPPED', 'Shipped'),
        ('DELIVERED', 'Delivered'),
        ('CANCELLED', 'Cancelled'),
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product, through='OrderItem')
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='PENDING')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def calculate_discount(self):
        """사용자 등급에 따른 할인율 계산"""
        if hasattr(self.user, 'profile') and self.user.profile.is_premium:
            return Decimal('0.10')  # 프리미엄 사용자 10% 할인
        return Decimal('0')  # 일반 사용자 할인 없음

    def calculate_total(self):
        """주문 총액 계산"""
        total = sum(item.get_subtotal() for item in self.orderitem_set.all())
        discount = self.calculate_discount()
        return total * (Decimal('1') - discount)

    def update_status(self, new_status):
        """주문 상태 변경 메서드"""
        # 상태 변경 유효성 검증
        valid_transitions = {
            'PENDING': ['PAID', 'CANCELLED'],
            'PAID': ['SHIPPED', 'CANCELLED'],
            'SHIPPED': ['DELIVERED'],
            'DELIVERED': [],  # 최종 상태
            'CANCELLED': []  # 최종 상태
        }

        if new_status not in valid_transitions[self.status]:
            raise ValidationError(f"Cannot transition from {self.status} to {new_status}")

        self.status = new_status
        self.save()

    def __str__(self):
        return f"Order {self.id} - {self.user.username}"


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    price_at_purchase = models.DecimalField(max_digits=10, decimal_places=2)

    def get_subtotal(self):
        """개별 상품의 소계 계산"""
        return self.price_at_purchase * self.quantity

    def save(self, *args, **kwargs):
        # 첫 저장 시 상품 가격을 저장
        if not self.pk:
            self.price_at_purchase = self.product.price
            # 재고 확인 및 차감
            self.product.reduce_stock(self.quantity)

        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.quantity}x {self.product.name} in Order {self.order.id}"