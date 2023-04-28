from django.shortcuts import render

# Create your views here.
from home.models import *

def name(request):
    student_info=Student.objects.all()
    return render(request,'name.html',{'student_info':student_info})
