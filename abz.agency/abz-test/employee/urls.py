from django.urls import path
from .views import *

urlpatterns = [
    path('', show_employee_list, name='employee_list'),
        
]