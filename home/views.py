from django.shortcuts import render, redirect
from admin_datta.forms import RegistrationForm, LoginForm, UserPasswordChangeForm, UserPasswordResetForm, UserSetPasswordForm
from django.contrib.auth.views import LoginView, PasswordChangeView, PasswordResetConfirmView, PasswordResetView
from django.views.generic import CreateView
from django.contrib.auth import logout

from django.contrib.auth.decorators import login_required
from .models import Lead
from .models import Contact
from .models import User
from .models import Activity


def index(request):
  users = User.objects.all().values()
  leads = Lead.objects.all().values()

  context = {
    'segment': 'index',
    'users': users,
    'leads': leads
  }
  return render(request, "pages/index.html", context)


def company(request, id):
  lead = Lead.objects.get(id=id)
  contacts = Contact.objects.filter(
    type=lead.lead_name).order_by('date').values()

  employees_count = len(User.objects.filter(company=lead.lead_name).values())

  company_tasks = Activity.objects.filter(company=lead.lead_name).values()

  today_task = company_tasks.filter(dateType="today")
  week_task = company_tasks.filter(dateType="week")
  users = User.objects.all().values()

  context = {
    'segment': 'index',
    'lead': lead,
    'contacts': contacts,
    'employees_count': employees_count,
    'today_task': today_task,
    'week_task': week_task,
    'company_tasks': company_tasks,
    'users': users,
  }
  return render(request, "pages/company.html", context)

# Authentication


class UserRegistrationView(CreateView):
  template_name = 'accounts/auth-signup.html'
  form_class = RegistrationForm
  success_url = '/accounts/login/'


class UserLoginView(LoginView):
  template_name = 'accounts/auth-signin.html'
  form_class = LoginForm


class UserPasswordResetView(PasswordResetView):
  template_name = 'accounts/auth-reset-password.html'
  form_class = UserPasswordResetForm


class UserPasswrodResetConfirmView(PasswordResetConfirmView):
  template_name = 'accounts/auth-password-reset-confirm.html'
  form_class = UserSetPasswordForm


class UserPasswordChangeView(PasswordChangeView):
  template_name = 'accounts/auth-change-password.html'
  form_class = UserPasswordChangeForm


def logout_view(request):
  logout(request)
  return redirect('/accounts/login/')


@login_required(login_url='/accounts/login/')
def profile(request):
  context = {
    'segment': 'profile',
  }
  return render(request, 'pages/profile.html', context)


@login_required(login_url='/accounts/login/')
def sample_page(request):
  context = {
    'segment': 'sample_page',
  }
  return render(request, 'pages/sample-page.html', context)
