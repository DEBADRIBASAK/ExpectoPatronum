from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from .models import Company
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.http import Http404,HttpResponse
from django.core.files.storage import FileSystemStorage
from django.conf import settings
import pandas as pd
import numpy as np
# Create your views here.
def register(request):
	#error = {}
	if request.method=='POST':
		#print("POST = ",request.POST)
		obj = User()
		obj.username = request.POST['Username']
		password = request.POST['Password']
		password2 = request.POST['Confirm Password']
		if(password!=password2):
			#error = {'password2':'the confirmation password does not match with the actual password'}
			return render(request,'register.html',{'is_wrong':True})
		obj.set_password(request.POST['Password'])
		obj.save()
		obj1 = Company()
		obj1.username = obj
		obj1.Name = request.POST['Name']
		#obj1.Organization = request.POST.get('Organization',False)#=='on'
		if 'Organization' in request.POST:
			obj1.Organization = True
		else:
			obj1.Organization = False
		obj1.PhoneNo = request.POST['Phone']
		obj1.EmailID = request.POST['EmailID']
		obj1.Fax = request.POST['Fax']
		obj1.save()
	return render(request,'register.html',{'is_wrong': False})

def LogIn(request):
	a = request.user.is_authenticated
	if a and request.user.is_staff:
		logout(request)
		return render(request,'home.html',{})
	elif a:
		usr = request.user
		obj = Company.objects.get(username=usr)
		return render(request,'profile.html',{'Company':obj})
	elif request.method=='POST':
		print("post============",request.POST)
		name = request.POST['username']
		passwrd = request.POST['password']
		try:
			obj1 = authenticate(username=name,password=passwrd)
			if obj1 is None:
				raise User.DoesNotExist
		except User.DoesNotExist:
			return HttpResponse('<h1>User does not exist!</h1>')
		login(request,obj1)
		obj2 = Company.objects.get(username=obj1)
		return render(request,'profile.html',{'Company': obj2})
	return render(request,'login.html',{})

def home(request):
	return render(request,'home.html',{})


def LogOut(request):
	logout(request)
	return redirect('/HRO/home')

def Upload(request):
	print("\n\n\nI am in upload")
	obj = request.user
	obj1 = Company.objects.get(username=obj)
	if request.method=='POST' and request.FILES:
		file = request.FILES.get('HR_Info')
		if file:
			fs = FileSystemStorage()
			path = 'docs/'+file.name
			obj1.HR_Info = path
			fs.save(path,file)
		obj1.save()
		return render(request,'profile.html',{'Company':obj1})
	return render(request,'upload.html',{})

def HR_Information(request):
	obj = request.user
	obj1 = Company.objects.get(username=obj)
	if request.method=='GET':
		if obj1.HR_Info:
			path = settings.MEDIA_ROOT+'/'+str(obj1.HR_Info)
			data = pd.read_csv(path)
			data = np.array(data)
			print('\n\n\n',data)
			return render(request,'info.html',{'data':data})
	return render(request,'profile.html',{'Company':obj1})