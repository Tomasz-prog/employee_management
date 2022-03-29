from django.contrib import admin
from django.urls import path, include
from .views import glowna
from . import views


app_name = 'employee'
urlpatterns = [
    path('', glowna, name='start'),
    path('register/', views.register_request, name='register'),
    path('login/', views.login_request, name='login_request'),
    path('logout/', views.logout_request, name='logout_request'),
    path('add-employee/', views.AddEmployee.as_view(), name='add_employee'),
    path('list_employee/', views.EmployeeView.as_view(), name='list_employee'),
    path('update_employee/<int:pk>/update/', views.EmployeeUpdate.as_view(), name='update_employee'),
    path('delete_employee/<int:pk>/delete/', views.EmployeeDelete.as_view(), name='delete_employee'),

    path('dept_create/', views.DeptCreate.as_view(), name='dept_create'),
    path('dept/<int:pk>/update/', views.DeptUpdate.as_view(), name='dept_update'),
    path('dept/<int:pk>/delete/', views.DeptDelete.as_view(), name='dept_delete'),
    path('dept_list', views.DeptView.as_view(), name='dept_list'),
]