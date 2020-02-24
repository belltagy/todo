from django.db import models

# Create your models here.
class List(models.Model):
	name=models.TextField(default='',null=True)
class Item(models.Model):
	text = models.TextField(default='');
	list = models.ForeignKey(List, on_delete=models.SET_NULL,null=True)

