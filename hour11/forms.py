from hour11.models import User11Hour
from django.contrib.auth.models import User 
from django import forms

class User11HourForm(forms.ModelForm):
	password = forms.CharField(widget = forms.PasswordInput())
	class Meta:
		model = User
		fields = ('first_name','last_name','username','email','password')

class User11HourProfileForm(forms.ModelForm):
	class Meta:
		model = User11Hour 
		fields = ('sex',)#,'picture')
