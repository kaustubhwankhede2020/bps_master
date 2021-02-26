from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from . import models
from django.urls import reverse

# Create your views here.

# Creating a rendering function which will render the login page for BPS Master
def render_login(request):
    return render(request, 'bosch_production_app/auth_templates/login.html')

# Creating a function which will perform the login functionality for BPS Master
def perform_login(request):
    if request.method != "POST":
        return HttpResponse("Method Not Allowed")
    else:
        print("Sign IN Initiated")
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        print(user)
        if user is not None:
            login(request, user)
            if user.user_type == "1":
                return HttpResponseRedirect("admin_home")
            if user.user_type == "2":
                return HttpResponse("Manager Login")
            if user.user_type == "3":
                return HttpResponse("Expert Login")
            if user.user_type == "4":
                return HttpResponseRedirect(reverse("operator_home"))
        else:
            messages.error(request, "Invalid Credentials")
            return HttpResponseRedirect("/")

# Creating a rendering function which will render the signup page for BPS Master
def render_signup(request):
    department_objs = models.Department.objects.all()
    context = {
        'departments': department_objs
    }
    return render(request, "bosch_production_app/auth_templates/signup.html", context)

# Creating a function which will perform the signup functionality for BPS Master
def perform_signup(request):
    if request.method != "POST":
        return HttpResponse("Method Not Allowed")
    else:
        print("Sign UP Initiated")
        firstname = request.POST.get("firstname")
        lastname = request.POST.get("lastname")
        username = request.POST.get("username")
        email = request.POST.get("email")
        employeenumber = request.POST.get("employee_number")
        department_id = request.POST.get("department")
        password = request.POST.get("password")
        confirm = request.POST.get("confirm_password")
        if confirm != password:
            messages.error(request,'Invalid password confirmation')
            return HttpResponseRedirect(reverse('signup'))
        else:
            try:
                print("Creating User")
                user_obj = models.CustomUser.objects.create_user(first_name=firstname, last_name=lastname, username=username, email=email,employee_number=employeenumber,password=password, user_type=4)
                user_obj.operator.department=models.Department.objects.get(main_id=department_id)
                user_obj.save()
                messages.success(request,'User created successfully !')
                return HttpResponseRedirect(reverse('signup'))
            except:
                messages.error(request,'User registration falied as user already exists !')
                return HttpResponseRedirect(reverse('signup'))

def perform_logout(request):
    logout(request)
    return HttpResponseRedirect("/")
