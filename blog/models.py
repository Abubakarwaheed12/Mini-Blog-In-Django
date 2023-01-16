from django.db import models

# Post models here.

class post(models.Model):
    title=models.CharField(max_length=170)
    desc=models.CharField(max_length=3000)