from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm

import pyrebase

config = {
    "apiKey": "AIzaSyAWiH8XoRRK5UQcc1aLBkMAP0hwFBLQET4",
    "authDomain": "axial-keep-231806.firebaseapp.com",
    "databaseURL": "https://axial-keep-231806.firebaseio.com",
    "projectId": "axial-keep-231806",
    "storageBucket": "axial-keep-231806.appspot.com",
    "messagingSenderId": "1005263861742",
    "appId": "1:1005263861742:web:114c61248c103e9f5480ff",
    "measurementId": "G-CLLJXNGKBH"
}

firebase = pyrebase.initialize_app(config)


def register(request):
    print("one")
    if request.method == 'POST':
        print("two")
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            print("three")
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            print("email was" + email)
            auth = firebase.auth()
            auth.create_user_with_email_and_password(email, password)
            #username = form.cleaned_data.get('username')
            messages.success(request, f'Your account has been created! You are now able to log in')
            return redirect('login')
        else:
            print(form.errors)
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})


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
            return redirect('profile')

    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form
    }

    return render(request, 'users/profile.html', context)
