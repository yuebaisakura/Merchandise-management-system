from django.db import models
from django.utils import timezone

class Product(models.Model):
    name = models.CharField(max_length=200, verbose_name='商品名称')
    description = models.TextField(verbose_name='商品描述')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='商品价格')
    stock = models.IntegerField(default=0, verbose_name='商品库存')
    image = models.ImageField(upload_to='products/', blank=True, null=True, verbose_name='商品图片')
    created_at = models.DateTimeField(default=timezone.now, verbose_name='创建时间')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='更新时间')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '商品'
        verbose_name_plural = '商品管理'
        ordering = ['-created_at']
