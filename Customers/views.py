from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from . models import Customer
# Create your views here.
def signout(request):
    logout(request)
    return redirect('home')
def signin(request):
    if request.POST and 'SIGNIN' in request.POST:
        # Handle login logic here
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username = username, password = password)
        # Authenticate the user
        if user:
            login(request,user)
            return redirect('home')
        else:
            messages.success(request, 'invaled username and passworld')
    return render(request, 'Login.html')

def signup(request):
    if request.POST and 'register' in request.POST:
        try:
            # Handle signup logic here
            username = request.POST.get('username')
            email = request.POST.get('email')
            phone = request.POST.get('phone')
            address = request.POST.get('address')
            password = request.POST.get('password')
            # Save the user data to the database or perform other actions
            # For example, create a new user object and save it
            user = User.objects.create_user(
                username=username,
                email=email,
                password=password
                )
            customer = Customer.objects.create(
                user=user,
                phone=phone,
                address=address
            )
            success = "Your login Succesefilly"
            messages.success(request, success)
        except Exception as e:
            error = "user name already exists "
            messages.error(request, error)
    return render(request, 'Signup.html')