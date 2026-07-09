from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class student(models.Model):
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    marks=models.IntegerField(
        validators=[
            MinValueValidator(0,message='Marks cannot be less than 0'),
            MaxValueValidator(100,message='Marks cannot be more yhan 100')
        ]
    )

def __str__(self):
    return self.name
