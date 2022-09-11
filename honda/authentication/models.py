from django.db import models

# Create your models here.
class Two_wheeler(models.Model):
    title = models.CharField(max_length=100)
    Totalstock = models.IntegerField(default=5)
    Available = models.IntegerField(default=5)
    Booked=models.IntegerField(default=0)
    bikeurl = models.CharField(default="a",max_length=100)

class Four_wheeler(models.Model):
    title=models.CharField(max_length=100)
    Totalstock = models.IntegerField(default=5)
    Available = models.IntegerField(default=5)
    Booked=models.IntegerField(default=0)
    carurl = models.CharField(default="a",max_length=100)

class staff(models.Model):
    username=models.CharField(max_length=100)
    staffname=models.CharField(max_length=100)
    staffAddress=models.CharField(max_length=100)
    staffpancard=models.CharField(max_length=100)
    staffaadharcardno=models.CharField(max_length=100)
    staffphoneno=models.CharField(max_length=100)
    password=models.CharField(max_length=100)

class Booking_by_customer(models.Model):
    customerID = models.IntegerField()
    StockID = models.IntegerField()
    StaffID = models.IntegerField()