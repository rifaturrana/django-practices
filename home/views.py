from django.shortcuts import render
from .models import *

# Create your views here.

def home(request):
    all_data=Contact.objects.all()
    return render(request,'home.html',{'all_data':all_data})
