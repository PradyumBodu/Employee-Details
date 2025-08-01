

from django.http import HttpResponse
from django.shortcuts import render
from employee_data.models import Employees


def home(request):
    employee = Employees.objects.all()
    return render(request,'home.html',{'employee':employee})