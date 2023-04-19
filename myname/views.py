from django.shortcuts import render

# Create your views here.

def name(request):
    return render(request,'name.html')
