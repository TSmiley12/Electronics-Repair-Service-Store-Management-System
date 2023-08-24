from django.urls import path
from . import views

urlpatterns = [
    path('register_problem/', views.register_problem, name='register_problem'),
    path('client_problems/', views.client_problems, name='client_problems'),
    path('problem_detail/<int:problem_id>/', views.problem_detail, name='problem_detail'),
    path('admin/problems_list/', views.admin_problems_list, name='admin_problems_list'),
    path('admin/assign_to_staff/<int:problem_id>/', views.assign_to_staff, name='assign_to_staff'),
    path('staff/problems/', views.staff_problem_list, name='staff_problem_list'),
    path('staff/mark_solved/<int:problem_id>/', views.mark_solved, name='mark_solved'),


]
