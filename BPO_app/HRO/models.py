from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Company(models.Model):
	username = models.OneToOneField(User,on_delete=models.CASCADE,primary_key=True,)
	Name = models.CharField(max_length=200,blank=False)
	Organization = models.BooleanField(default=True)
	HR_Info = models.FileField(upload_to='docs/')
	PhoneNo = models.CharField(max_length=10,blank=False,default=None)
	EmailID = models.CharField(max_length=200,blank=False,default=None)
	Fax = models.CharField(max_length=10,blank=False,default=None)
	def __str__(self):
		return str(self.Name)