from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from .forms import SignUpForm, EditPasswordForm
from django.contrib.auth.models import User
from django.views.generic.edit import UpdateView
from .models import Profile, Branch, Languages
from .forms import UserUpdateForm, ProfileUpdateForm
from django.contrib.auth.decorators import login_required


def profile(request):
    context = {'user': request.user}
    return render(request, 'authenticate/profile.html', context)

def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, ('You have been logged in!'))
            return redirect('authenticate:home')
        else:
            messages.success(request, ('Error logging in - Please try again!'))
            return redirect('authenticate:login')
    else:
        return render(request, 'authenticate/login.html')

def logout_user(request):
    logout(request)
    messages.success(request, ('You have been logged out!'))
    return redirect('core:home')

def register_user(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, ('You have been logged in!'))
                return redirect('core:home')
    else:
        form = SignUpForm()

    context = {'form': form}
    return render(request, 'authenticate/register.html', context)

'''
def edit_profile(request):
    if request.method == 'POST':
        form = EditProfileForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, ('You have been Edited your profile!'))
            return redirect('authenticate:home')
    else:
        form = EditProfileForm(instance=request.user)

    context = {'form': form}
    return render(request, 'authenticate/edit_profile.html', context)
'''

def change_password(request):
    if request.method == 'POST':
        form = EditPasswordForm(data=request.POST, user=request.user)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user) # so that id doesnt log out after password change
            messages.success(request, ('You have Changed your Password!'))
            return redirect('core:home')
    else:
        form = EditPasswordForm(user=request.user)

    context = {'form': form}
    return render(request, 'authenticate/change_password.html', context)

'''
def profile_edit(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=request.user.profile)
        if form.is_valid():
            form.save()
            messages.success(request, ('Your credentials have been saved!'))
            return redirect('authenticate:home')
    else:
        form = ProfileForm(data=request.POST)

    context = {'form': form}
    return render(request, 'authenticate/profile_edit.html', context)
'''

@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST,
                                   request.FILES,
                                   instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('authenticate:home')

    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form
    }

    return render(request, 'authenticate/profile.html', context)
    