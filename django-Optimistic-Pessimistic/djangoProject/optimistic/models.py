from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField()
    # 버전 필드
    version = models.PositiveIntegerField(default=0)

    def save(self, *args, **kwargs):
        # 새 객체가 아니라면 버전 증가
        if self.pk is not None:
            self.version += 1
        super().save(*args, **kwargs)