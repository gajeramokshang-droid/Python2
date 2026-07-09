from django.db import models
from django.core.validators import MinValueValidator,MaxValueValidator

class Course(models.Model):
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    marks=models.IntegerField(validators=[
        MinValueValidator(0,"Min length cannot be less than 0"),
        MaxValueValidator(100,"Max length cannot be gt than 100")
    ]
    )