from django.urls import path
from . import views

urlpatterns = [
path('register/',views.register,name='register'),
path('home/',views.home,name='home'),
path('log_in/',views.LogIn,name='log_in'),
path('logout/',views.LogOut,name='log_out'),
path('upload/',views.Upload,name='upload'),
path('Info/',views.HR_Information,name='show'),
]