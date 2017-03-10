from __future__ import unicode_literals

from django.db import models


# Create your models here.
class login_gw(models.Model):
	name = models.CharField(max_length=30)
	pwd = models.CharField(max_length=100)
	address = models.CharField(max_length=300)
	email = models.EmailField()


	def __str__(self):
		return self.name
