from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from . import models
from datetime import datetime
from django.contrib import messages
from django.urls import reverse

# Create your views here.

def render_operator_home(request):
    return render(request, 'bosch_production_app/operator_templates/operator_home.html')

def render_operator_dashboard(request):
    return render(request, 'bosch_production_app/operator_templates/operator_dashboard.html')

def render_production_entry(request):
    return render(request, 'bosch_production_app/operator_templates/production_entry.html')

def render_laser_production(request):
    return render(request, 'bosch_production_app/operator_templates/laser_production.html')

def render_internal_grinding(request):
    return render(request, 'bosch_production_app/operator_templates/internal_grinding.html')

def render_external_grinding(request):
    return render(request, 'bosch_production_app/operator_templates/external_grinding.html')

def render_chamfer_grinding(request):
    return render(request, 'bosch_production_app/operator_templates/chamfer_grinding.html')

def render_aqueous_cleaning(request):
    return render(request, 'bosch_production_app/operator_templates/aqueous_cleaning.html')

def render_operator_profile(request):
    return render(request, 'bosch_production_app/operator_templates/operator_profile.html')
