from django.shortcuts import render
from django.shortcuts import render
from .models import Employe
from .forms import EmpForm

# Create your views here.


def add(request):
    empForm=EmpForm()
    return render(request,'add.html',{'empForm':empForm})

def get(request):
    employees = Employe.objects.all()
    return render(request,'get.html',{'employees':employees})

def insertEmp(request):
    if request.method == "POST":
        empForm = EmpForm(request.POST)
        if empForm.is_valid():
            empForm.save()
            return render(request,'get.html')
        else:
            return render(request,'add.html')
    else:
        return render(request,'add.html')
    

def editEmp(request,eid):
    emp = Employe.objects.get(eid=eid)
    return render(request,'edit.html',{'emp':emp})

def updateEmp(request,eid):
    if request.method == "POST":
        emp = Employe.objects.get(eid=eid)
        form = EmpForm(request.POST,instance=emp)
        if form.is_valid():
            form.save()
            return render(request,'get.html')
        else:
            return render(request,'edit.html',{'emp':emp,'msg':'Details Not Updated...!!!'})
    else:
        return render(request,'edit.html',{'emp':emp,'msg':'Details Not Updated...!!!'})

def deleteEmp(request,eid):
    emp = Employe.objects.get(eid=eid)
    emp.delete()
    return render(request,'get.html')