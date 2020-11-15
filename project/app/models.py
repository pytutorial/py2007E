from django.db import models

# Create your models here.
class Category(models.Model):
    code = models.CharField(max_length=30, verbose_name='Mã', unique=True)
    name = models.CharField(max_length=200, verbose_name='Tên')
    def __str__(self):
        return self.name

class Product(models.Model):
    code = models.CharField(max_length=30,verbose_name='Mã',  unique=True)
    name = models.CharField(max_length=200, verbose_name='Tên')
    description = models.CharField(max_length=500, verbose_name='Mô tả',  blank=True)
    price = models.FloatField(verbose_name='Giá')
    category = models.ForeignKey(Category, verbose_name='Nhóm', on_delete=models.PROTECT)
    image = models.ImageField(verbose_name='Ảnh', upload_to='static/images')
    def __str__(self):
        return self.name

class Order(models.Model):
    class Status:
        NEW = 0
        DELIVERED = 1
        CANCELED = 2

    product = models.ForeignKey(Product,on_delete=models.PROTECT)
    qty = models.IntegerField()
    customer_name = models.CharField(max_length=50)
    customer_phone = models.CharField(max_length=20)
    customer_address = models.CharField(max_length=200)
    order_date = models.DateTimeField()
    deliver_date = models.DateTimeField(null=True)
    status = models.IntegerField()

