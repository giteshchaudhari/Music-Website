from django.shortcuts import render
from .forms import UserForm
from song.models import Geet
from django.http import HttpResponseRedirect,HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login,logout
# Create your views here.
@login_required
def user_logout(request):
	logout(request)
	context={}
	context["database"]=Geet.objects.all()
	return render(request,"account/index.html",context)
	
def register(request):
	form=UserForm(request.POST or None)
	if form.is_valid() :
		user=form.save(commit=False)
		username = form.cleaned_data['username']
		password = form.cleaned_data['password']
		user.set_password(password)
		user.save()
		user = authenticate(username=username, password=password)
	context={
	"form":form,
	}
	return render(request ,'account/register.html',context)

def user_login(request):

	if request.method=='POST':
		username=request.POST.get('username')
		password=request.POST.get('password')

		user=authenticate(username=username,password=password)

		if user:
			if user.is_active:
				login(request,user)
				return HttpResponseRedirect(reverse('index'))
			else:
				return render(request, 'account/login.html', {'error_message': 'Your account has been disabled'})
		else:
			return render(request, 'account/login.html', {'error_message': 'Invalid login'})

	else:
		return render(request,'account/login.html')
