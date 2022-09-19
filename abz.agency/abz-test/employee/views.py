from django.shortcuts import render
from .models import *


def show_employee_list(request):
    employees = Employee.objects.all()
    return render(request, 'employee/employee_list.html', context={'employee_list': employees})



