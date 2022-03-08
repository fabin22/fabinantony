from django.db import models

class student(models.Model):
     name=models.CharField(max_length=100)
     username=models.CharField(max_length=100)
     password=models.CharField(max_length=100)
     dob=models.DateField()
     mark=models.IntegerField()