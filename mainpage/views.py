from django.shortcuts import render,get_object_or_404, redirect, HttpResponseRedirect
from .models import File,Contact
from.forms import Forms



def mainpage(request):
	data = get_object_or_404(File, id=2)
	# datas = get_object_or_404(Contact)
	form = Forms(request.POST or None)
	if form.is_valid():
		forms = form.save(commit=False)
		forms.save()
	return render(request, 'mainpage.html', {'data': data,'form':form,})

def message(request):
	contact=Contact.objects.all()
	return render(request,'contacts.html',{'contact':contact})

def project(request):
	contact=Contact.objects.all()
	return render(request,'project.html',{})

