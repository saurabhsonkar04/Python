from django.shortcuts import render,redirect
from .forms import EmployeeForm,LoginForm
from .models import Employee

# Create your views here.
def employee_form(request,id=0):
   
    if request.method == "GET":
        #Normal Chrome open
        if id==0:
            form = EmployeeForm()
        else:
             #Update Logic
            employee = Employee.objects.get(pk=id)
            form = EmployeeForm(instance = employee)
        return render(request,"employee_register/employee_form.html",{'form':form})
    else:
        #New Registration
        form = EmployeeForm(request.POST)
        form.save() #to save into DB 
        employee = Employee.objects.get(pk=request.POST.get('empid'))
        form = EmployeeForm(instance=employee, data=request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.tutor = request.user
            instance.save()
        request.session["id"] = request.POST.get('empid') 
        return redirect('/employee/dashboard')

def employee_dashboard(request):
    employee = Employee.objects.get(pk= request.session["id"])
    return render(request,"employee_register/employee_dashboard.html",{'employee':employee})


def employee_delete(request,id):
    employee = Employee.objects.get(pk= id)
    form = EmployeeForm(instance = employee)
    employee.delete()
    return render(request,"employee_register/employee_form.html",{'form':form})

def employee_login(request):
        if request.method == "POST":
            form = LoginForm(data=request.POST)
            if form.is_valid:
                request.session["id"] = request.POST.get('empid')
                return redirect('/employee/dashboard')
        else:
            form = LoginForm()
            return render(request,"employee_register/employee_login.html",{'form':form})


