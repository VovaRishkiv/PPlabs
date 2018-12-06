from django.db import models

# Create your models here.

class Rating(models.Model):
    class Meta:
        db_table = "rating"
    group = models.CharField(max_length = 50)
    name = models.CharField(max_length = 50)
    mark = models.CharField(max_length = 50)
