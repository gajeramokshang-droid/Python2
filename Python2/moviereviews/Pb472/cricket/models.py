from django.db import models

class Cricket(models.Model):
    name = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    batting = models.CharField(max_length=100)
    bowling = models.CharField(max_length=100)
    age = models.IntegerField()
    runs = models.IntegerField()
    wickets = models.IntegerField()

    def __str__(self):
        return self.name
