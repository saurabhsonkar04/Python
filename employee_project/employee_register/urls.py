from django.urls import path,include
from . import views

urlpatterns = [
    path('registration', views.employee_form,name='employee_insert' ),
    path('<int:id>/',views.employee_form,name='employee_update'),
    path('dashboard/',views.employee_dashboard, name = 'employee_dashboard'),
    path('delete/<int:id>/',views.employee_delete,name = 'employee_delete'),
    path('login/',views.employee_login,name = 'employee_login')
    
]
