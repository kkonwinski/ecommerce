from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponseRedirect
from .forms import LoginForm, RegisterForm

# Display the login page
def login_page(request):
    return render(request, 'accounts/login.html')

# Handle the registration process
def register_page(request):
    register_form = RegisterForm()
    if request.method == 'POST':
        register_form = RegisterForm(request.POST)
        if register_form.is_valid():
            user = register_form.save(commit=False)
            user.username='{} {}'.format(register_form.cleaned_data['first_name'], register_form.cleaned_data['last_name'])
            user.set_password(register_form.cleaned_data['password1'])
            user.save()
            messages.success(request, 'Your account has been created. Please login.')
            return HttpResponseRedirect('login')

    return render(request, 'accounts/register.html', {'form': register_form})
