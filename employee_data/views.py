from django.http import HttpResponse
from django.shortcuts import redirect, render
from .models import Employees
from .forms import EmployeeForms

# Create your views here.
def add(request):

    if request.method == 'POST':
        form = EmployeeForms(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = EmployeeForms()
    return render(request,'add.html',{'form':form})
    

def delete(request,pk):
    form = Employees.objects.get(pk=pk)
    form.delete()
    return redirect('home')
    
def update(request,pk):
    employee = Employees.objects.get(pk=pk)
    if request.method == 'POST':
        form = EmployeeForms(request.POST,instance=employee)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = EmployeeForms(instance=employee)
    return render(request,'update.html',{'form':form,'employee':employee})