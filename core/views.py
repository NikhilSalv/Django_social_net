from django.shortcuts import render, HttpResponse, redirect
from .models import Profile
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.contrib.auth.decorators import login_required
import string

# Create your views here.
@login_required(login_url='signin')
def index(request):
    return render(request, 'index.html')

def signup(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]
        password = request.POST["password"]
        confirm_pass = request.POST["confirm_pass"]

        def is_strong_password(password):
            has_upper = any(c.isupper() for c in password)
            has_lower = any(c.islower() for c in password)
            has_special = any(c in string.punctuation for c in password)
            has_digit = any(c.isdigit() for c in password)
            return has_upper and has_lower and has_special and has_digit
        
        if password != confirm_pass:
            messages.info(request,"Password does not match")
            return redirect('signup')
        
        else:
            if User.objects.filter(username=username).exists():
                messages.info(request, "Username taken")
                return redirect('signup')
            if User.objects.filter(email=email).exists():
                messages.info( request,"Email taken")
                return redirect('signup')
            if not is_strong_password(password):
                messages.info(request, "Password is weak")
                return redirect('signup')
            
        user = User.objects.create_user(username=username, email=email, password=password)
        Profile.objects.create(user=user, id_user=user.id)

        messages.info(request, "Congratulations !! User Created")
        return redirect('signup')


    else:
        return render(request, 'signup.html')
    

def signin(request):
        
    if request.method == 'POST':
        username  = request.POST["username"]
        password  = request.POST["password"]

        user = auth.authenticate(username=username, password=password)
        # all_users = User.objects.all()

        if user:
            auth.login(request,user)
            # auth.login
            return redirect('index')
        else:
            messages.info(request, "User not found")
            return redirect('signin')

    else:
        return render(request, 'signin.html')

@login_required(login_url='signin')    
def logout(request):
    auth.logout(request)
    return redirect( 'signin' )

@login_required(login_url='signin')
def settings(request):
    return render(request,"setting.html")