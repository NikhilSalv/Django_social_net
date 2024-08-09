from django.shortcuts import render, HttpResponse, redirect
from .models import Profile, Post, LikedPost, FollowCount
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.contrib.auth.decorators import login_required
import string



# Create your views here.
@login_required(login_url='signin')
def index(request):

    user_object = User.objects.get(username = request.user.username)

    user_profile = Profile.objects.get(user=request.user)

    posts = Post.objects.all()
    return render(request, 'index.html', {"user_profile": user_profile, "posts" : posts})


@login_required(login_url='signin')
def upload(request):
    if request.method == "POST":
        print("Post updating...")
        user = request.user.username
        image = request.FILES.get("image_upload")
        caption = request.POST.get("caption")
        print("values fetched ...", caption)

        new_post = Post.objects.create(user=user, caption= caption, image = image)
        print("Post updated...")
        new_post.save()
        print("Post uploaded")

        return redirect("index")

    else:
        return redirect("index")

@login_required(login_url='signin')
def like_post(request):
    username = request.user.username
    post_id = request.GET.get("post_id")

    post = Post.objects.get(id= post_id)

    like_filter = LikedPost.objects.filter(post_id=post_id, username= username).first()

    if like_filter == None:
        new_like = LikedPost.objects.create(post_id=post_id, username= username)
        new_like.save()

        post.no_of_likes += 1
        post.save()
        return redirect("index")
    else:
        like_filter.delete()
        post.no_of_likes -= 1
        post.save()
        print("4 . The Logged in user name in Liked Post is : ", username)
        return redirect("index")

@login_required(login_url='signin')
def profile(request,pk):
    print("Data from FE for Logged in User Profile is : " , pk)
    user_object = User.objects.get(username=pk)
    # print("Logged in User is : " , user_object.username)
    user_profile = Profile.objects.get(user=user_object)
    user_posts = Post.objects.filter(user=pk)
    user_post_len = len(user_posts)


    follower = request.user.username
    user = pk

    if FollowCount.objects.filter(follower=follower, user=user).first():
        button_text = "Unfollow"
    else:
        button_text = "Follow"

    user_followers = len(FollowCount.objects.filter(user=pk))
    user_following = len(FollowCount.objects.filter(follower=pk))

    context = {
        "user_object" : user_object,
        "user_profile" : user_profile,
        "user_posts" : user_posts,
        "user_post_len" : user_post_len,
        "button_text": button_text,
        "user_followers": user_followers,
        "user_following" : user_following
    }
    return render(request, "profile.html", context)


@login_required(login_url='signin')
def follow(request):
    if request.method == "POST":
        follower = request.POST["follower"]
        user = request.POST["user"]
        print("user is  : ", user, "follower is :", follower)

        if FollowCount.objects.filter(follower = follower, user = user).first():
            delete_follower = FollowCount.objects.get(follower = follower, user = user)
            delete_follower.delete()
            return redirect("profile", pk=user)
        else:
            new_follower = FollowCount.objects.create(follower = follower, user = user)
            new_follower.save()
            return redirect("profile", pk=user)

        # loggedin_user = User.objects.get(usename=user)
        # loggedin_user_profile = Profile.objects.get(user=loggedin_user)

    else:
        return redirect("profile", pk=user)


def signup(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]
        password = request.POST["password"]
        confirm_pass = request.POST["confirm_pass"]

        
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
        user_login = auth.authenticate(username=username, password=password)
        auth.login(request, user_login)

        Profile.objects.create(user=user, id_user=user.id)

        # messages.info(request, "Congratulations !! User Created")
        return redirect('settings')


    else:
        return render(request, 'signup.html')
    

def is_strong_password(password):
            has_upper = any(c.isupper() for c in password)
            has_lower = any(c.islower() for c in password)
            has_special = any(c in string.punctuation for c in password)
            has_digit = any(c.isdigit() for c in password)
            return has_upper and has_lower and has_special and has_digit


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
    user_profile = Profile.objects.get(user=request.user)

    if request.method == "POST":
        if request.FILES.get("image") == None:
            image = user_profile.profile_img
            bio = request.POST.get("bio")
            location = request.POST.get("location")

            user_profile.profile_img = image
            user_profile.bio = bio
            user_profile.location = location
            user_profile.save()

        if request.FILES.get("image") != None:
            image = request.FILES.get("image")
            bio = request.POST.get("bio")
            location = request.POST.get("location")

            user_profile.profile_img = image
            user_profile.bio = bio
            user_profile.location = location
            user_profile.save()

        return redirect("settings") 
    return render(request,"setting.html", {"user_profile" : user_profile})