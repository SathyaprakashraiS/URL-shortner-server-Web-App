from django.db import models

# Create your models here.
class Url(models.Model):
	url=models.CharField(max_length=1000,default="url")
	murl=models.CharField(max_length=1000,default="murl")
	done=models.IntegerField(default=1)