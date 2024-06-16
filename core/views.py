from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
    return render(request, 'index.html')

def signup(request):
    if request.method == "POST":
        username = request.POST.get("username")
        return HttpResponse("user name is : ", username)
    else:
        return render(request, 'signup.html')