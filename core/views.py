from django.shortcuts import render, HttpResponse, redirect
from .models import Profile
from django.contrib.auth.models import User, auth
from django.contrib import messages

# Create your views here.
def index(request):
    return render(request, 'index.html')

def signup(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]
        password = request.POST["password"]
        confirm_pass = request.POST["confirm_pass"]

        if password == confirm_pass:
            if User.objects.filter(username=username).exists():
                messages.info(request, "Username taken")
                return redirect('signup')
            if User.objects.filter(email=email).exists():
                messages.info( request,"Email taken")
                return redirect('signup')
            else:
                user = User.objects.create_user(username=username, email=email, password=password)
                user.save()

                user_model = User.objects.get(username=username)
                profile_user = Profile.objects.create(user=user_model, id_user=user_model.id)
                profile_user.save()

                messages.info(request, "Congratulations !! User Created")
                return redirect('signup')
            
        
        else:
            messages.info(request,"Password does not match")
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
    
def logout(request):
    auth.logout(request)
    return redirect( 'signin' )