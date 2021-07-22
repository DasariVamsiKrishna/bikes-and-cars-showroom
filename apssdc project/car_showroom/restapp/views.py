from django.shortcuts import render,redirect
from django.http import HttpResponse
from restapp.forms import UsgForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required 
from restapp.forms import cars
from restapp.models import cars
from restapp.models import buycar
from restapp.forms import orderscars
from django.contrib.auth.decorators import login_required




# Create your views here.

@login_required
def home(request):
    return render(request,'html/home.html')




def reg(request):
	if request.method == "POST":
		d = UsgForm(request.POST)
		if d.is_valid():
			d.save()
			return redirect('/login')
	d = UsgForm()
	return render(request,'html/reg.html',{'t':d})

@login_required
def car(request):

    y = cars.objects.all()
    return render(request,'html/car.html',{'q':y})



def support(request):
    return render(request,'html/support.html')


def buycars(request,a):
	if request.method == "POST":
		t = orderscars(request.POST)
		if t.is_valid():
			t.save()
			return redirect('/thankyou')
	t = orderscars()
	s = cars.objects.get(id=a)
	return render(request,'html/buycars.html',{'z':s ,'q':t})


def thankyou(request):
	return render(request,'html/thankyou.html')



def services(request):
	return render(request,'html/services.html')

@login_required
def logout(request):
	return render(request,'html/logout.html')