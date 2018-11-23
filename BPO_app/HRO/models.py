from django.db import models
from django.contrib.auth.models import User
import datetime
from django.core.validators import MaxValueValidator,MinValueValidator
# Create your models here.
class Company(models.Model):
	company_code = models.CharField(max_length=20,blank=False,default=None,primary_key=True)
	username = models.OneToOneField(User,on_delete=models.CASCADE)
	Name = models.CharField(max_length=200,blank=False)
	HR_Info = models.FileField(upload_to='docs/')
	PhoneNo = models.CharField(max_length=10,blank=False,default=None)
	EmailID = models.CharField(max_length=200,blank=False,default=None)
	def __str__(self):
		return str(self.Name)

class Employee(models.Model):
	#EmployeeCode = models.CharField(max_length=20,blank=False)
	username = models.OneToOneField(User,on_delete=models.CASCADE)
	company = models.ForeignKey(Company,on_delete=models.CASCADE,default=None)
	Name = models.CharField(max_length=200,blank=False)
	PhoneNo = models.CharField(max_length=10,blank=False,default=None)
	EmailID = models.CharField(max_length=200,blank=False,default=None)
	Deposit = models.IntegerField(default=10000)
	HCARequest = models.IntegerField(default=1)
	RequestAmount = models.IntegerField(default=0)
	def __str__(self):
		return str(self.Name)

class BPO_Employee(models.Model):
	EmployeeCode = models.CharField(max_length=20,blank=False,primary_key=True)
	Name = models.CharField(max_length=200)
	choices = (("INST","Installation"),
		("SURV","Surveillance"),
		("MAIN","Maintenance"),
		)
	EmpType = models.CharField(max_length=15,choices=choices,default="INST")
	Charge = models.IntegerField(default=10000)
	isAvail = models.BooleanField(default=True)
	ch = (('M','Male'),('F','Female'),)
	Gender = models.CharField(max_length=10,choices=ch,default='M')
	PhoneNo = models.CharField(max_length=10,blank=False,default=None)
	EmailID = models.CharField(max_length=200,blank=False,default=None)
	Rating = models.IntegerField(default=0,validators=[MinValueValidator(0),MaxValueValidator(5)])
	def __str__(self):
		return str(self.Name)

class AccountingInfo(models.Model):
	company_code = models.ForeignKey(Company,on_delete=models.DO_NOTHING)
	date = models.IntegerField(default=int(datetime.date.today().year))
	info = models.FileField(upload_to='ecmdocs/')

