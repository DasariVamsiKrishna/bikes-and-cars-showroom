from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm
from restapp.models import cars
from restapp.models import buycar
from restapp.models import orders



class UsgForm(UserCreationForm):
	password1 = forms.CharField(widget=forms.PasswordInput(attrs={
		"class":"form-control my-2","placeholder":"Enter Password",
		}))
	password2 = forms.CharField(widget=forms.PasswordInput(attrs={
		"class":"form-control my-2","placeholder":"Enter Confirm Password",
		}))
	class Meta:
		model = User
		fields = ["username"]
		widgets = {
		"username":forms.TextInput(attrs={
			"class":"form-control my-2",
			"placeholder":"Enter Username",
			}),
		}




class Reform(ModelForm):
	class Meta:
		model = cars
		fields = "__all__"

class orderscars(ModelForm):
	class Meta:
		model = orders
		fields =["carnames","carmodels","carcolours","deliveryaddress"]
		widgets = {
			"carnames":forms.TextInput(attrs={
				"class":"form-control my-2",
				"placeholder":"Enter the car name",

			}),
			"carmodels":forms.NumberInput(attrs={
				"class":"form-control my-2",
				"placeholder":"enter the model",
			}),
			"carcolours":forms.TextInput(attrs={
				"class":"form-control my-2",
				"placeholder":"enter the colour",
			}),
			"deliveryaddress":forms.TextInput(attrs={
				"class":"form-control my-2",
				"placeholder":"enter the delivery address",
				"rows":5,
			}),
		}
		


		
