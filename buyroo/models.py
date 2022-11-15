from django.db import models
from django.contrib.auth.models import User
#class names should be capitalized while fields are in lowercase
# Create your models here.

class Category(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='products', default= 'pix.jpg')
    
    def __str__(self):
        return self.title

    class Meta:
        db_table ='Category'
        managed = True
        verbose_name ='Category'
        verbose_name_plural ='Categories'

    
class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    price = models.FloatField()
    image = models.ImageField(upload_to='products', default='pix.jpg')
    description = models.TextField()
    featured = models.BooleanField()
    latest = models.BooleanField()
    available = models.BooleanField()
    women_dress = models.BooleanField(default=False)
    women_blouse = models.BooleanField(default=False)
    boy_shirt = models.BooleanField(default=False)
    boy_pant = models.BooleanField(default=False)
    men_jacket = models.BooleanField(default=False)
    men_trench = models.BooleanField(default=False)
    girl_dress = models.BooleanField(default=False)
    girl_skirt = models.BooleanField(default=False)
    min = models.IntegerField()
    max = models.IntegerField()

    def __str__(self):
        return self.name


class MyCart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    basket_no = models.CharField(max_length=50)
    quantity = models.IntegerField()
    paid_order = models.BooleanField()

    def __str__(self):
        return self.user.username

class Payment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.IntegerField()
    basket_no = models.CharField(max_length=50)
    pay_code = models.CharField(max_length=50)
    paid_order = models.BooleanField()
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    country = models.CharField(max_length=50)

    def __str__(self):
        return self.user.username
    