from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import ProblemForm
from django.contrib.auth.decorators import user_passes_test
from .models import Problems_section
from django.shortcuts import render, get_object_or_404
from accounts.models import User
# @login_required


def is_client(user):
    return user.client_is == True
    # return hasattr(user, 'client_is')


def is_staff(user):
    return user.staff_is == True


def is_admin(user):
    return user.client_is == user.staff_is == False


@user_passes_test(is_client, login_url='/accounts/home/')  # Redirect to login
def register_problem(request):
    if request.method == 'POST':
        form = ProblemForm(request.POST)
        if form.is_valid():
            problem = form.save(commit=False)
            problem.client = request.user.client
            problem.save()
            return redirect('client_problems')  # Redirect to a success page
    else:
        form = ProblemForm()

    context = {'form': form}
    return render(request, 'myapp/register_problem.html', context)


@user_passes_test(is_client, login_url='/accounts/home/')
def client_problems(request):
    problems = Problems_section.objects.filter(client=request.user.client)
    return render(request, 'client/client_problems.html', {'problems': problems})


@user_passes_test(is_client, login_url='/accounts/home/')
def problem_detail(request, problem_id):
    problem = get_object_or_404(
        Problems_section, id=problem_id, client=request.user.client)
    return render(request, 'client/problem_detail.html', {'problem': problem})


# ----------------------------------------------------------------------

@user_passes_test(is_admin, login_url='/accounts/home/')
def admin_problems_list(request):
    problems = Problems_section.objects.all()
    context = {'problems': problems}
    return render(request, 'myapp/admin_problems_list.html', context)


@user_passes_test(is_admin, login_url='/accounts/home/')
def assign_to_staff(request, problem_id):
    problem = Problems_section.objects.get(id=problem_id)
    staff_users = User.objects.filter(staff_is=True)  # Get all staff users

    if request.method == 'POST':
        staff_id = request.POST.get('staff_id')
        staff = User.objects.get(id=staff_id)
        problem.staff_involved.clear()
        problem.staff_involved.add(staff)
        # Redirect back to the admin's problem list page
        return redirect('admin_problems_list')

    context = {'problem': problem, 'staff_users': staff_users}
    return render(request, 'myapp/assign_to_staff.html', context)

# ------------------------------------------


@user_passes_test(is_staff, login_url='/accounts/home/')
def staff_problem_list(request):
    staff = request.user  # Get the logged-in staff member
    problems = Problems_section.objects.filter(staff_involved=staff)
    return render(request, 'myapp/staff_problem_list.html', {'problems': problems})


@user_passes_test(is_staff, login_url='/accounts/home/')
def mark_solved(request, problem_id):
    problem = Problems_section.objects.get(id=problem_id)
    problem.solved = True
    problem.save()
    return redirect('staff_problem_list')
