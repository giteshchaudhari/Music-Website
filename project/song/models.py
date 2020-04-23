from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Geet(models.Model):
	title=models.CharField(max_length=200)
	track=models.FileField(upload_to='track/',null=True)
	author=models.ForeignKey(User,default=None,on_delete=models.CASCADE)
	artist=models.CharField(max_length=250,default=' ')
	is_favorite=models.BooleanField(default=False)
	def __str__(self):
		return self.title + ' - ' + self.artist  