from django.db import models

# Create your models here.
class cars(models.Model):
    carname = models.CharField(max_length=30)
    carmodel = models.IntegerField()
    carcolor = models.CharField(max_length=20)
    carprice = models.IntegerField()
    carimage = models.ImageField(upload_to='carimage/',default='defaultcar.jpg')


class buycar(models.Model):
    cnames = models.CharField(max_length=20,default='carnames') 
    cmodel = models.IntegerField(default='2021')
    ccolor = models.CharField(max_length=20,default='carcolour')
    cprice = models.IntegerField(default='1000000')
    address = models.CharField(max_length=50)

    
    
class orders(models.Model):
    carnames = models.CharField(max_length=30)
    carmodels = models.IntegerField()
    carcolours = models.CharField(max_length=30)
    carprice = models.IntegerField(default='100000')
    deliveryaddress = models.CharField(max_length=100)