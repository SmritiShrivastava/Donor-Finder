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
        print("Ch")
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
        confirm_Password = request.POST['confirm_Password']
        print(password, confirm_Password)
        if password == confirm_Password:
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
    if not request.user.is_authenticated:
        if request.method == "POST":
            form = logInForm(request.POST)
            if form.is_valid():
                username = form.cleaned_data.get('username')
                password = form.cleaned_data.get('password')
                if userProfiles.objects.filter(username = username).exists():
                    queryset = userProfiles.objects.get(username = username)
                    user = authenticate(request, username = username, password = password)
                    if user is not None:
                        login(request, user)
                        context={
                            'models':queryset,
                        }
                        return render(request, "detail.html",context)
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
    else:
        return redirect('donate')

def logoutView(request):
	if request.user.is_authenticated:
		logout(request)
		return redirect("home")
	else:
		return redirect("login")

def detailView(request):
    if request.user.is_authenticated:
        return render(request, "detail.html")

def donateView(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            form = donorForm(request.POST)
            if form.is_valid():
                donated = form.cleaned_data.get('donated')
                drinked = form.cleaned_data.get('drinked')
                disease = form.cleaned_data.get('disease')
                bloodgroupuser = userProfiles.objects.get(username = request.user)
                bloodGroup = bloodgroupuser.bloodGroup
                if donated is True and drinked is True and disease is True:
                    object = donorModel.objects.create(
                        donated = donated,
                        drinked = drinked,
                        disease = disease,
                        userkey = userProfiles.objects.get(username = request.user),
                        bloodGroup = bloodGroup
                    )
                    object.save()
                    messages.success(request, "Congratulations, You are all set to become somesone's donor and save a life")
                    return redirect("detail")
            else:
                messages.info(request, "You are not allowed to donate blood now")
                return redirect(donateView)
        else:
            form = donorForm()
            context = {
                'form': form,
                'models':userProfiles.objects.get(username = request.user),
            }
            return render(request, "donate.html", context)

def findDonorView(request):
    if request.user.is_authenticated:
        return render(request, "receive.html")

def receiveView(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            search = request.POST['search']
            print(search)
            queryset = {}
            if search == " ":
                pass
            else:
                queryset = userProfiles.objects.filter(bloodGroup__iexact = search)
                print(queryset)
            context = {
                'models': queryset
            }
            return render(request, "donor.html", context)
        else:
            form = searchForm()
            return redirect(request, 'receive')