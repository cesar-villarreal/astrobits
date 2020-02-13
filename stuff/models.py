from django.db import models

# Create your models here.

class Picture(models.Model):
	picture_url = models.CharField(max_length=150)
	picture_thumbnail = models.CharField(max_length=150)
	picture_description = models.CharField(max_length=200)