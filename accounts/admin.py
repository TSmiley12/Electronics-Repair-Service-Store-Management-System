from django.contrib import admin
from .models import User, Client, Staff


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'client_is', 'staff_is')


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('user', 'phone_number')


@admin.register(Staff)
class StaffAdmin(admin.ModelAdmin):
    list_display = ('user', 'phone_number')


# Register your models here.
