from django.contrib.auth.forms import UserCreationForm
from django.db import transaction
from django import forms
from .models import Client, Staff, User


class ClientSignUpForm(UserCreationForm):
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    phone_number = forms.CharField(required=True)

    class Meta(UserCreationForm.Meta):
        model = User

    @transaction.atomic
    def data_save(self):
        user = super().save(commit=False)
        user.first_name = self.cleaned_data.get('first_name')
        user.last_name = self.cleaned_data.get('last_name')
        user.client_is = True
        user.save()
        client = Client.objects.create(user=user)
        client.phone_number = self.cleaned_data.get('phone_number')
        client.save()
        return user


class StaffSignUpForm(UserCreationForm):
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    phone_number = forms.CharField(required=True)

    class Meta(UserCreationForm.Meta):
        model = User

    @transaction.atomic
    def data_save(self):
        user = super().save(commit=False)
        user.first_name = self.cleaned_data.get('first_name')
        user.last_name = self.cleaned_data.get('last_name')
        user.staff_is = True
        user.save()
        staff = Staff.objects.create(user=user)
        staff.phone_number = self.cleaned_data.get('phone_number')
        staff.save()
        return user
