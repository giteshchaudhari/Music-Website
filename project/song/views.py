from django.shortcuts import render,redirect,get_object_or_404
from song.models import Geet
from song.forms import GeetForm
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView,DetailView
from django.contrib.auth.models import User
from django.http import HttpResponse
# Create your views here.  
def Index(request):
	context={}
	context["database"]=Geet.objects.all()
	return render(request,"account/index.html",context)

class AboutView(TemplateView):
	template_name='song/about.html'

@login_required
def MyGeetList(request):
	context={}
	context["database"]=Geet.objects.filter(author=request.user)
	return render(request,'song/my_geet_list.html',context)

@login_required
def CreateGeetView(request):
	if request.method == 'POST':
		form = GeetForm(request.POST, request.FILES)
		if form.is_valid():
			instance=form.save(commit=False)
			instance.author=request.user
			instance.save()
			return redirect('index')
	else:
		form = GeetForm()
	return render(request, 'song/geet_create.html', {'form': form })

@login_required
def GeetDeleteView(request,pk):
	context={}
	obj=get_object_or_404(Geet,pk=pk)
	obj.delete()   
	context["database"]=Geet.objects.filter(author=request.user)
	return  render(request,"song/my_geet_list.html",context)

@login_required
def Favourite(request,pk):
	geet=get_object_or_404(Geet,pk=pk)
	if geet.is_favorite:
		geet.is_favorite=False
	else:
		geet.is_favorite=True
	geet.save()
	context={}
	context["database"]=Geet.objects.all()
	return render(request,"account/index.html",context)


