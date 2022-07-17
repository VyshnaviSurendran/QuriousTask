from msilib.schema import Class
from django.db import models

# Create your models here.
class Manager(models.Model):
    FullName = models.CharField(max_length=20)
    Photo = models.ImageField(upload_to='media')
    ContactNumber = models.CharField(max_length=13)
    EmailAddress = models.CharField(max_length=20)
    Username = models.CharField(max_length=20)
    Password = models.CharField(max_length=8)

class Coordinator(models.Model):
    FullName = models.CharField(max_length=20)
    Photo = models.ImageField(upload_to='media')
    ContactNumber = models.CharField(max_length=13)
    EmailAddress = models.CharField(max_length=20)
    Username = models.CharField(max_length=20)
    Password = models.CharField(max_length=8)

class Inspector(models.Model):
    FullName = models.CharField(max_length=20)
    Photo = models.ImageField(upload_to='media')
    ContactNumber = models.CharField(max_length=13)
    EmailAddress = models.CharField(max_length=20)
    Username = models.CharField(max_length=20)
    Password = models.CharField(max_length=8)

class ClientMaster(models.Model):
    SLNo = models.IntegerField()
    ClientName = models.CharField(max_length=20)
    Location = models.CharField(max_length=50)

class JobMaster(models.Model):
    scheduledDate = models.DateField()
    inspector = models.ForeignKey(Inspector,on_delete=models.CASCADE)
    clientname = models.ForeignKey(ClientMaster,on_delete=models.CASCADE)
    clientlocation = models.CharField(max_length=20)