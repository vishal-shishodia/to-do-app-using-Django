from django.shortcuts import render,redirect
from .models import Task
from .forms import TaskForm

def index(request):
	tasks=Task.objects.all()
	form=TaskForm()
	if request.POST:
		form=TaskForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('/')
	else:
		context={'tasks':tasks,'form':form}
		return render(request,'tasks/list.html',context)

def UpdateTask(request,pk):
	task=Task.objects.get(id=pk)
	form=TaskForm(instance=task)
	if request.POST:
		form=TaskForm(request.POST,instance=task)
		if form.is_valid():
			form.save()
			return redirect('/')
	else:
		context={'form':form}
		return render(request,'tasks/update_task.html',context)

def Delete(request,pk):
	item=Task.objects.get(id=pk)
	if request.POST:
		item.delete()
		return redirect('/')
	context={'item':item}
	return render(request,'tasks/delete.html',context)
	