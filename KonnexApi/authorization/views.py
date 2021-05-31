from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .forms import UserRegistrationForm
from faq.models import Questions, Answers

# def register_start(request):
#     if request.method == 'GET':

def register(request):
    
    answers = get_object_or_404(Answers, byUser__username = request.POST.get("username"))
    questions = get_object_or_404(Questions,title = "q1")
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            userregister = form.save(commit=False)
            userregister.questions = questions
            userregister.answers = answers
            form.save()

            username = form.cleaned_data.get('username')
            messages.success(request, f'Account Created for {username}!')
            return redirect('register')

    else:
        form = UserRegistrationForm()    

    
    return render(request, 'authorization/register.html', {'form' : form})




