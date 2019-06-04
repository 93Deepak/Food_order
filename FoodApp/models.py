from django.db import models

# Create your models here.
class Product(models.Model):
    pname=models.CharField(max_length=30)
    opt=(('rte','Ready To Eat'),('rtd','Ready To Drink'))
    category=models.CharField(max_length=3,choices=opt,default='rte')
    price=models.FloatField()
    description=models.CharField(max_length=100)
    pic=models.FileField(upload_to='images/')
    def get_absolute_url(self):
        return reverse('detail',kwargs={'pk':self.pk})

class Cart(models.Model):
    pid=models.IntegerField()
    name=models.CharField(max_length=30)
    quantity=models.IntegerField()
    price=models.FloatField()
    total=models.FloatField()
    user=models.CharField(max_length=30)
    pic=models.CharField(max_length=30)
    def __str__(self):
        return self.pid

class OrderTable(models.Model):
    pid=models.IntegerField()
    name=models.CharField(max_length=30)
    quantity=models.IntegerField()
    price=models.FloatField()
    total=models.FloatField()
    user=models.CharField(max_length=30)
    pic=models.CharField(max_length=30)
    status=models.IntegerField()
    date=models.DateField(auto_now_add=True)

class total(models.Model):
    total=models.FloatField()
