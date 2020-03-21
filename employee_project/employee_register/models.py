from django.db import models

class Department(models.Model):
    depid = models.IntegerField(primary_key=True)
    depname = models.CharField(max_length=1000)
    def __str__(self):
        return self.depname

class Manager(models.Model):
    managid = models.IntegerField(primary_key=True)
    managerName = models.CharField(max_length=1000)
    def __str__(self):
        return self.managerName

# Create your models here.
class Employee(models.Model):
    fname = models.CharField(max_length=100)
    email = models.CharField(max_length=1000)
    empid = models.IntegerField(primary_key=True)
    jobtitle = models.CharField(max_length=100)
    depname = models.ForeignKey(Department,on_delete=models.CASCADE)
    hiredate = models.DateField((""), auto_now=False, auto_now_add=False)
    lastappraisaldate = models.DateField((""), auto_now=False, auto_now_add=False)
    reportingmanagername = models.ForeignKey(Manager,on_delete=models.CASCADE)
    evaluatedby = models.CharField(max_length=1000)

class Goal(models.Model):
    empid = models.ForeignKey(Employee,on_delete=models.CASCADE)
    goalid = models.CharField(max_length=1000,primary_key=True)
    goaltitle = models.CharField(max_length=1000)
    goaldesc = models.CharField(max_length=10000)
    duedate = models.DateField((""), auto_now=False, auto_now_add=False)
    empcmt = models.CharField(max_length=10000)
    managcmt = models.CharField(max_length=10000)
    stars =  models.IntegerField()

class Login(models.Model):
    empid =  models.IntegerField()
    password  = models.CharField(max_length=1000)
    def __str__(self):
        return self.empid
