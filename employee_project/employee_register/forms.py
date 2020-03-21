from django import forms
from .models import Employee,Login


class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = '__all__'
        labels = {
            'fname' : 'Full Name',
            'email' : 'Email',
            'empid' : 'Employee ID',
            'jobtitle' : 'Job Tilttle',
            'depname' : 'Department Name',
            'hiredate' : 'Hire Date',
            'lastappraisaldate' : 'Last Appraisal Date',
            'reportingmanagername' : 'Reporting Manager Name',
            'evaluatedby' : 'Evaluated By'
        }
    def __init__(self,*args,**kwargs):
        super(EmployeeForm,self).__init__(*args,**kwargs)
        self.fields['depname'].empty_label = "Select"
        self.fields['reportingmanagername'].empty_label = "Select"
        self.fields['evaluatedby'].required = False
        self.fields['lastappraisaldate'].required = False
        
class LoginForm(forms.ModelForm):
     class Meta:
        model = Login
        fields = '__all__'
        labels = {
            'empid' : 'Employee ID',
            'password' : 'Password'}
        
        def __init__(self,*args,**kwargs):
            super(EmployeeForm,self).__init__(*args,**kwargs)