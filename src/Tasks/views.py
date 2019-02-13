from django.shortcuts import render,redirect
from .models import List
from .forms import ListForm
from django.contrib import messages
# Create your views here.
def home(request):
	# return render(request,"home.html",{})
	if request.method == "POST" :
		form=ListForm(request.POST or None)
		if form.is_valid():
			form.save()
			messages.success(request,('Item has been added to your to-do list:'))
	all_items=List.objects.all()
	context={"all_items":all_items}
	return render(request,"home.html",context) 

def delete(request,id):
	obj=List.objects.get(id=id)
	obj.delete()
	messages.success(request,('Item has been deleted'))
	return redirect('home')

def cross_off(request,id):
	obj=List.objects.get(id=id)
	obj.completed=True 
	obj.save()
	return redirect('home')
def uncross(request,id):
	obj=List.objects.get(id=id)
	obj.completed=False
	obj.save()
	return redirect('home')
def edit(request,id):
	obj=List.objects.get(id=id)
	if request.method=="POST":
		form=ListForm(request.POST or None, instance=obj)
		if form.is_valid():
			form.save()
			messages.success(request,('Item has been edited:'))
			return redirect('home')
	else:
	    return render(request,"edit.html",{"item":obj})

