from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('login/', views.login_user, name='login_user'),
    path('logout/', views.logout_user, name='logout_user'),
    path('home/', views.home, name='home'),
    path('client_register/', views.client_register.as_view(),
         name='client_register'),
    path('staff_register/', views.staff_register.as_view(),
         name='staff_register'),

    path('login_client/', views.login_client, name='login_client'),
    path('login_staff/', views.login_staff, name='login_staff'),




]
