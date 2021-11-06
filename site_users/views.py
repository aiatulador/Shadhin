from django.contrib import auth
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import UseRegistrationForm
from .forms import UserUpdateForm, UserJobSetForm, ProfileUpdateFrom
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import get_user, authenticate, login
from .models import Profile

from django.core.mail import send_mail
from post_work.models import PostWork
from django.template.loader import render_to_string
from django.conf import settings


def base(request):
    return render(request, 'users/base.html')


@login_required
def profile(request):
    return render(request, 'users/profile.html')


@login_required
def profile_update(request):

    if len(Profile.objects.filter(user=request.user)) == 0:
        profile = Profile(user = request.user)
        profile.save()

    if request.method == 'POST':
        user_update_form = UserUpdateForm(request.POST, instance=request.user)
        profile_update_form = ProfileUpdateFrom(request.POST, request.FILES, instance=request.user.profile)

        if user_update_form.is_valid() and profile_update_form.is_valid():
            user_update_form.save()
            profile_update_form.save()

            return redirect('profile')
        else:
            context = {
                'user_update_form': user_update_form,
                'profile_update_form': profile_update_form

            }
            return render(request, 'users/profile_update.html', context)
    else:
        user_update_form = UserUpdateForm(instance=request.user)
        profile_update_form = ProfileUpdateFrom()

        context = {
            'user_update_form': user_update_form,
            'profile_update_form': profile_update_form
        }
        return render(request, 'users/profile_update.html', context)


def about(request):
    return render(request, 'users/about.html')


def contract(request):
    return render(request, 'users/contract.html')


def register(request):
    if request.method == "POST":
        reg_form = UseRegistrationForm(request.POST)

        if reg_form.is_valid():
            reg_form.save()
            # username = reg_form.cleaned_data.get('username')
            # password = reg_form.cleaned_data.get('password1')
            # us = authenticate(username=username, password=password)
            # auth.login(request, us)
            return redirect('login')
        else:
            context = {
                'form': reg_form
            }
            return render(request, 'users/register.html', context)

    else:
        reg_form = UseRegistrationForm()
        context = {
            'form': reg_form
        }

        return render(request, 'users/register.html', context)


def login(request):
    if request.method=='POST':

        UserReg = get_user(request)
        context = {
        'name': UserReg.username,
        'email': UserReg.email,
        }

        subject = "Shadhin"
        body = render_to_string('user/intro_email.html')
        send_mail(
            subejct,
            body,
            settings.EMAIL_HOST_user
            [UserReg.email]
        )

    return render(request, 'users/login.html', context)


@login_required
def job_set(request):
    if request.method == "POST":
        set_form = UserJobSetForm(request.POST)
        if set_form.is_valid():
            set_form.save()
            return redirect('work')
        else:
            set_form = UserJobSetForm()
            context = {
                'form': set_form
            }
            return render(request, 'users/job_set.html', context)

    else:
        set_form = UserJobSetForm()
        context = {
            'form': set_form
        }
        return render(request, 'users/job_set.html', context)


@login_required
def find_work(request):
    from post_work.models import PostWork
    pw = PostWork.objects.all()

    return render(request, 'users/find_work.html', {'pw':pw})








