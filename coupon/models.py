from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class Coupon(models.Model):
    code = models.CharField(max_length=50,
                            unique=True,
                            verbose_name="Промокод")
    valid_from = models.DateTimeField(verbose_name="Начало акции")
    valid_to = models.DateTimeField(verbose_name="Действует до")
    discount = models.IntegerField(
        validators=[MinValueValidator(0),
                    MaxValueValidator(100)],
        verbose_name="Скидка")
    active = models.BooleanField(verbose_name="Статус")

    def __str__(self):
        return self.code
