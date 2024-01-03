from django.shortcuts import redirect,render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

# Create your views here.
def home(request):
    return render(request, "index.html")

def signup(request):

    if request.method == 'POST':
        username = request.POST['username']
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['username']
        password = request.POST['password']
        confirmpw = request.POST['confirmpw']

        myuser = User.objects.create_user(username, fname, email)
        myuser.save()

        messages.success(request, "account created")

        return redirect('signin')

    return render(request, "signup.html")

def signin(request): 

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        user = authenticate(username = username, password = password)

        if user is not None:
            login(request, user)
            fname = user.first_name
            return render(request, 'index.html', {'fname': fname})

        else:
            messages.error(request, 'Bad Credentials')
            return redirect('home')
    

    return render(request, "signin.html")

def signout(request):
    pass