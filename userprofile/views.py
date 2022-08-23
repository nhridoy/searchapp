from django.shortcuts import render, HttpResponseRedirect, reverse, redirect
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from userprofile.models import User, Profile
from userprofile.forms import EditProfileForm, LoginForm, RegistrationForm
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import logout, login, authenticate
from django.views.generic import ListView, CreateView, UpdateView, TemplateView, DetailView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin


# Create your views here.
def login_executed(redirect_to):
    """This Decorator kicks authenticated user out of a view"""

    def _method_wrapper(view_method):
        def _arguments_wrapper(request, *args, **kwargs):
            if request.user.is_authenticated:
                return redirect(redirect_to)
            return view_method(request, *args, **kwargs)

        return _arguments_wrapper

    return _method_wrapper


@login_executed('searchapp:index')
def registrationView(request):
    form = RegistrationForm()
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return HttpResponseRedirect(reverse('searchapp:index'))
    context = {
        'form': form,
        'title': 'Register Now',
        'button': 'Register',
    }
    return render(request, 'authenticate.html', context)


@login_executed('searchapp:index')
def loginView(request):
    form = LoginForm()
    error_messages = None

    if request.method == 'POST':
        form = LoginForm(request.POST)
        username, password = request.POST.get('username'), request.POST.get('password')
        if user := authenticate(username=username, password=password):
            login(request, user)
            return HttpResponseRedirect(reverse('searchapp:index'))
        else:
            error_messages = "Email or Password Invalid. Note that both fields maybe case sensitive."

    context = {
        'form': form,
        'title': 'Login Now',
        'error_message': error_messages,
        'button': 'Login',
    }
    return render(request, 'authenticate.html', context)


@login_required
def userProfileView(request):
    context = {

    }
    return render(request, 'profile.html', context)


@login_required
def editProfileView(request):
    current_user = request.user
    form = EditProfileForm(instance=current_user.user_profile)
    if request.method == 'POST':
        form = EditProfileForm(request.POST, request.FILES, instance=current_user.user_profile)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('profileapp:profile'))
    context = {
        'form': form,
        'title': 'Edit Profile',
    }
    return render(request, 'edit.html', context)


@login_required
def changePassView(request):
    current_user = request.user
    form = PasswordChangeForm(user=current_user)
    if request.method == 'POST':
        form = PasswordChangeForm(data=request.POST, user=current_user)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('profileapp:profile'))
    context = {
        'form': form,
        'title': 'Change Password',
    }
    return render(request, 'edit.html', context)


@login_required
def logoutView(request):
    logout(request)
    return HttpResponseRedirect(reverse('searchapp:index'))
