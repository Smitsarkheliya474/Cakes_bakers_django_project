from django.db import models

GENDER_CHOICES = (
    ('gender', 'Male'),
    ('gender', 'Female'),
)
class register(models.Model):
    firstname = models.CharField(max_length=20)
    email = models.CharField(max_length=50)
    password = models.CharField(max_length=10)
    gender = models.CharField(choices=GENDER_CHOICES,max_length=128)
    
    
class Admin_Detail(models.Model):
    name = models.CharField(max_length=20)
    email = models.CharField(max_length=50)
    contact = models.CharField(max_length=50)
    password = models.CharField(max_length=10)