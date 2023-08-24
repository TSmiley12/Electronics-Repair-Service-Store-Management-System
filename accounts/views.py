from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from django.views.generic import CreateView
from .models import User
from .forms import ClientSignUpForm, StaffSignUpForm
from django.db import IntegrityError
# from django.views.decorators.csrf import csrf_exempt  # careful


def home(request):
    if request.user.is_authenticated and request.user.client_is == True:
        return redirect('client_problems')
    elif request.user.is_authenticated and request.user.staff_is == True:
        return redirect('staff_problem_list')
    else:
        return render(request, 'home.html')


def register(request):
    return render(request, 'register.html')


class client_register(CreateView):
    model = User
    form_class = ClientSignUpForm
    template_name = 'client_register.html'

    def form_valid(self, form):
        try:
            user = form.save()
            form.data_save()
            login(self.request, user)
            return redirect('/accounts/home')
        except IntegrityError:
            form.add_error(
                'username', 'Username already exists. Please choose a different username.')
            return self.form_invalid(form)


class staff_register(CreateView):
    model = User
    form_class = StaffSignUpForm
    template_name = 'staff_register.html'

    def form_valid(self, form):
        try:
            user = form.save()
            form.data_save()
            login(self.request, user)
            return redirect('/accounts/home')
        except IntegrityError:
            form.add_error(
                'username', 'Username already exists. Please choose a different username.')
            return self.form_invalid(form)


def login_user(request):
    return render(request, 'login.html')


def logout_user(request):
    logout(request)
    return redirect('/accounts/home')

# -----------------------------------------------


# @csrf_exempt  # careful
def login_client(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None and user.client_is:
                login(request, user)
                # Redirect to client home page
                # return redirect('/accounts/home')
                return redirect('client_problems')  # working on it
            else:
                messages.error(request, "Invalid username or password")
        else:
            messages.error(request, "Invalid username or password")
    return render(request, 'accounts/client_login.html', context={'form': AuthenticationForm()})


def login_staff(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None and user.staff_is:
                login(request, user)
                # Redirect to staff home page
                return redirect('/accounts/home')
            else:
                messages.error(request, "Invalid username or password")
        else:
            messages.error(request, "Invalid username or password")
    return render(request, 'staff_login.html', context={'form': AuthenticationForm()})
