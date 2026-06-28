from django.db import models
from django.contrib.auth.models import User

class Hotel(models.Model):
    name=models.CharField(max_length=100)
    location=models.CharField(max_length=100)
    description=models.TextField()
    
def __str__(self):
    return f"{self.name} - {self.location}"


class Booking(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    guests=models.IntegerField()
    check_in=models.DateField()

