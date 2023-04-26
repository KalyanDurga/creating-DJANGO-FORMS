from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from app.forms import *


def student(request):
    SD=Studentdetails()
    d={'SD':SD}

    if request.method=='POST':
        FD=Studentdetails(request.POST)
        if FD.is_valid():
            print(FD)
            return HttpResponse(str(FD.cleaned_data))

            
    return render(request,'student.html',d)
