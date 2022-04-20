from math import perm
from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError

from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse

from .models import User
from .forms import PatientRegistrationForm, ConsultantRegistrationForm

# Create your views here.
def home_view(request):
    try: 
        User.objects.get(pk=request.user.id)
        consultant = User.objects.get(pk=request.user.id)
        context = {
            'qualification': consultant.qualification
        }
        return render(request, "users/index.html", context)
    except User.DoesNotExist:
        return render(request, "users/index.html")

def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        print(username)
        print(password)
        user = authenticate(request, username=username, password=password)
        print(user)

        # Check if authentication successful
        if user is not None:
            if user.is_staff:
                return render(request, "users/login.html", {
                    "message": "Admin not allowed to log in"
                })
            else:
                login(request, user)
                print("logged in")
                return HttpResponseRedirect(reverse("home"))
        else:
            return render(request, "users/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "users/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("home"))


def patient_register_view(request):
    if request.method == "POST":
        form = PatientRegistrationForm(request.POST)

        if form.is_valid():
            extra_fields = {
                'first_name': form.cleaned_data["first_name"],
                'last_name': form.cleaned_data["last_name"],
                'is_patient': True
            }
            username = form.cleaned_data["username"]
            email = form.cleaned_data["email"]

            # Ensure password matches confirmation
            password = form.cleaned_data["password"]
            confirmation = form.cleaned_data["confirm_password"]
            if password != confirmation:
                return render(request, "users/register.html", {
                    "userform": form,
                    "message": "Passwords must match."
                })

            # Attempt to create new user
            try:
                user = User.objects.create_user(username, email, password, **extra_fields)
                user.save()
            except IntegrityError:
                return render(request, "users/register.html", {
                    "userform": form,
                    "message": "Username already taken."
                })
            login(request, user)
            return HttpResponseRedirect(reverse("home"))
        else:
            return render(request, "users/register.html", {
                "userform": form,
                "message": "Form error"
            })
    else:
        form = PatientRegistrationForm()
        return render(request, "users/register.html",{
            "userform": form
        })

def consultant_register_view(request):
    if request.method == "POST":
        form = ConsultantRegistrationForm(request.POST)

        if form.is_valid():
            extra_fields = {
                'first_name': form.cleaned_data["first_name"],
                'last_name': form.cleaned_data["last_name"],
                'qualification': form.cleaned_data["qualification"],
                'is_consultant': True
            }
            username = form.cleaned_data["username"]
            email = form.cleaned_data["email"]

            # Ensure password matches confirmation
            password = form.cleaned_data["password"]
            confirmation = form.cleaned_data["confirm_password"]
            if password != confirmation:
                return render(request, "users/register.html", {
                    "consultantform": form,
                    "message": "Passwords must match."
                })

            # Attempt to create new user
            try:
                user1 = User.objects.create_user(username, email, password, **extra_fields)
                user1.save()
            except IntegrityError:
                print(extra_fields)
                print(username)
                return render(request, "users/register.html", {
                    "consultantform": form,
                    "message": "Username already taken."
                })
            login(request, user1)
            print("logged in")
            return HttpResponseRedirect(reverse("home"))
        else:
            return render(request, "users/register.html", {
                "consultantform": form,
                "message": "Form error"
            })
    else:
        form = ConsultantRegistrationForm()
        return render(request, "users/register.html",{
            "consultantform": form
        })
