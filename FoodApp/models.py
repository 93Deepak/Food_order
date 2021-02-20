from django.db import models

# Create your models here.


class Product(models.Model):
    pname = models.CharField(max_length=30)
    opt = (('rte', 'Ready To Eat'), ('rtd', 'Ready To Drink'))
    category = models.CharField(max_length=3, choices=opt, default='rte')
    price = models.FloatField()
    description = models.CharField(max_length=100)
    pic = models.FileField(upload_to='images/')

    def get_absolute_url(self):
        return reverse('detail', kwargs={'pk': self.pk})


class Cart(models.Model):
    pid = models.IntegerField()
    name = models.CharField(max_length=30)
    quantity = models.IntegerField()
    price = models.FloatField()
    total = models.FloatField()
    user = models.CharField(max_length=30)
    pic = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class CartTotal(models.Model):
    master_total = models.FloatField(null=True)
    master_quantity = models.FloatField(null=True)
    user = models.CharField(max_length=30)

    def __str__(self):
        return self.master_total


class OrderTable(models.Model):
    pid = models.IntegerField()
    name = models.CharField(max_length=30)
    quantity = models.IntegerField()
    price = models.FloatField()
    total = models.FloatField()
    user = models.CharField(max_length=30)
    pic = models.CharField(max_length=30)
    opt = (('Pending', 'Pending'), ('Dispatched',
                                    'Dispatched'), (' ', 'delivered'))
    status = models.CharField(max_length=20, choices=opt, default='Pending')
    opts = ((' ', 'pending'), ('Dispatched from Source', 'Dispatched'), ('Reaching Destination',
                                                                         'reaching'), ('Reached Destination', 'reached'), ('Delivered', 'deliverd'))
    detail = models.CharField(max_length=30, choices=opts, default='pending')
    date = models.DateField(auto_now_add=True)


class total(models.Model):
    total = models.FloatField()
