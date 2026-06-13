from django.shortcuts import render, redirect

from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.conf import settings
from django.utils.http import url_has_allowed_host_and_scheme

from .forms import RegisterForm


def register_view(request):

    if request.method == 'POST':

        form = RegisterForm(request.POST)

        if form.is_valid():
            form.save()

            return redirect('login')

    else:
        form = RegisterForm()

    return render(request, 'users/register.html', {
        'form': form
    })


def login_view(request):

    if request.user.is_authenticated:
        return redirect(settings.LOGIN_REDIRECT_URL)

    if request.method == 'POST':

        form = AuthenticationForm(request, data=request.POST)

        if form.is_valid():

            user = form.get_user()

            login(request, user)

            next_url = request.GET.get('next')

            if next_url and url_has_allowed_host_and_scheme(
                next_url,
                allowed_hosts={request.get_host()}
            ):
                return redirect(next_url)

            return redirect(settings.LOGIN_REDIRECT_URL)

    else:
        form = AuthenticationForm(request)

    return render(request, 'users/login.html', {
        'form': form
    })


def logout_view(request):

    logout(request)

    return redirect('login')
