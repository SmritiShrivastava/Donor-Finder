from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from .forms import *
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout

# Create your views here.
def homeView(request):
    return render(request, "home.html")

def signUpView(request):
    if request.method == "POST":
        username = request.POST['username']
        if userProfiles.objects.filter(username = username).exists():
            messages.info(request, "username already exists")
            return redirect("signup")
        firstName = request.POST['firstName']
        lastName = request.POST['lastName']
        bloodGroup = request.POST['bloodGroup']
        gender = request.POST['gender']
        age = request.POST['age']
        contactNumber = request.POST['contactNumber']
        password = request.POST['password']
        confirmPassword = request.POST['confirmPassword']
        if password == confirmPassword:
            object = userProfiles()
            object.username = username
            object.firstName = firstName
            object.lastName = lastName
            object.bloodGroup = bloodGroup
            object.gender = gender
            object.age = age
            object.contactNumber = contactNumber
            object.set_password(password)
            object.save()
            message_string = "Thank You" + username
            messages.success(request, message_string)
            return redirect("home")
        else:
            messages.warning(request, "Password doesn't matched")
            return redirect("signup")
    else:
        form = signUpForm()
        context = {
            'form': form
        }
        return render(request, "signUp.html", context)

def logInView(request):
    if request.method == "POST":
        form = logInForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            if userProfiles.objects.filter(username = username).exists():
                user = authenticate(request, username = username, password = password)
                if user is not None:
                    login(request, user)
                    return redirect("home")
                else:
                    messages.info(request, "username and password doesn't maatch")
                    return redirect("login")
            else:
                messages.info(request, "username doesn't exists")
                return redirect("signup")
        else:
            messages.info(request, "something went wrong")
            return redirect("login")
    else:
        form = logInForm()
        context = {
            'form': form
        }
        return render(request, "logIn.html", context)

