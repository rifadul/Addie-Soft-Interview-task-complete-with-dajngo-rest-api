from django.db import models

# Create your models here.

class Sales (models.Model):
    customerName = models.CharField(max_length=30)
    mobileNo = models.CharField(max_length=30)
    totalAmount = models.FloatField()

    def __str__(self):
        return self.customerName

class Product (models.Model):
    productName = models.CharField(max_length=30)
    ProductDetails = models.CharField(max_length=30)
    productPrice = models.FloatField()

    def __str__(self):
        return self.productName

class SalesDetails(models.Model):
    salesId = models.ForeignKey(Sales,related_name='salesby',on_delete=models.CASCADE)
    productId = models.ForeignKey(Product,related_name='productby', on_delete=models.CASCADE)
    quantity = models.FloatField()
    unitPrice = models.FloatField()
    total = models.FloatField()

class Album(models.Model):
    album_name = models.CharField(max_length=100)
    artist = models.CharField(max_length=100)
    
class Track(models.Model):
    album = models.ForeignKey(Album, related_name='tracks', on_delete=models.CASCADE)
    order = models.IntegerField()
    title = models.CharField(max_length=100)
    duration = models.IntegerField()

    class Meta:
        unique_together = ['album', 'order']
        ordering = ['order']

    def __str__(self):
        return '%d: %s' % (self.order, self.title)