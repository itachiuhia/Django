from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegistrationForm, UserUpdateForm, ProfileUpdateForm
from .models import Profiles, User
# from django.http import request



def register(request):
    if request.method == 'POST' :
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            userName = form.cleaned_data.get('username')
            messages.success(request, f'Your Account has been created with {userName}!')
            return redirect('login')
    else:
        form = UserRegistrationForm()

    
    return render(request, 'users/register.html',{'form': form})

@login_required
def profile(request):

    # prf = Profiles(user=request.user)

    if request.method == 'POST' :
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profiles)

        if u_form.is_valid() and p_form.is_valid() :
            u_form.save()
            p_form.save()

            # Profiles.objects.create(**{'user': user})

            messages.success(request, f'Your Account has been update !')
            # profiles.obeject

            return redirect('profile')
    else:

        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profiles)    
    

    context = {
        'u_form' : u_form,
        'p_form' : p_form
    }
    return render(request, 'users/profile.html', context)
