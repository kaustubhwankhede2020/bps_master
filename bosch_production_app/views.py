from django.shortcuts import render

# Create your views here.

# Creating a rendering function which will render the login page for BPS Master
def render_login(request):
    return render(request, 'bosch_production_app/auth_templates/login.html')

# Creating a rendering function which will render the admin home page for BPS Master
def render_admin_home(request):
    return render(request, 'bosch_production_app/admin_templates/admin_home.html')