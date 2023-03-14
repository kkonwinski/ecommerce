from django.shortcuts import render
from django.contrib import messages
from django.contrib.auth.models import User

# Create your views here.
def login_page(request):
    return render(request, 'accounts/login.html')


def register_page(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        password = request.POST['password']

        # Check if user already exists
        if User.objects.filter(username=email).exists():
            messages.error(request, 'User already exists')
            return redirect('register')

        # Create user object
        user = User.objects.create_user(
            username=email,
            first_name=first_name,
            last_name=last_name,
            email=email,
            password=password
        )

        messages.success(request, 'Your account has been created. Please login.')
        return redirect('login')

    return render(request, 'accounts/register.html')