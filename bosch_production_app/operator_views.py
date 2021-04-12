from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from . import models
from datetime import datetime
from django.contrib import messages
from django.urls import reverse
from .models import Machines, Components

# Create your views here.

def render_operator_home(request):
    if request.user.is_anonymous:
        return redirect("/")
    return render(request, 'bosch_production_app/operator_templates/operator_home.html')

def render_operator_dashboard(request):
    if request.user.is_anonymous:
        return redirect("/")
    return render(request, 'bosch_production_app/operator_templates/operator_dashboard.html')

def render_laser_production(request):
    if request.user.is_anonymous:
        return redirect("/")
    else:
        shift_objs = models.Shifts.objects.all()
        machine_objs = models.Machines.objects.all()
        component_objs = models.Components.objects.all()
        laser_production_objs = models.Laser_production.objects.all()
        params = {
            'shifts' : shift_objs,
            'machines' : machine_objs,
            'components' : component_objs,
            'laser_productions' : laser_production_objs
        }
        return render(request, 'bosch_production_app/operator_templates/laser_production.html', params)

def register_laser_production(request):
    if request.method != "POST":
        return HttpResponse("Method not Allowed")
    else:
        Laser_production_obj = models.Laser_production.objects.create(employee_id = request.POST.get("employee_id"), shift_id = models.Shifts.objects.get(main_id = request.POST.get("shift_code")), machine_id = models.Machines.objects.get(main_id=request.POST.get("machine_number")), component_id = models.Components.objects.get(main_id = request.POST.get("component_type")), component_lot_number = request.POST.get("component_lot_number"), component_quantity = request.POST.get("component_quantity"), created_at=datetime.now(), updated_at=datetime.now())
        Laser_production_obj.save()
        messages.success(request, "Laser Production Registered Sucessfully !")
        return HttpResponseRedirect(reverse('operator_laser_production'))

def render_edit_laser_production(request, main_id):
    if request.user.is_anonymous:
        return redirect("/")
    else:
        laser_production_obj = models.Laser_production.objects.get(main_id = main_id)
        context = {'laser_production' : laser_production_obj, 'laser_production_id' : main_id}
        print(laser_production_obj)
        return render(request,"bosch_production_app/operator_templates/edit_laser_production.html",context)

def edit_laser_production(request):
    if request.method!="POST":
        return HttpResponse("<h2>Method Not Allowed</h2>")
    else:
        main_id = request.POST.get('main_id')
        employee_id = request.POST.get('employee_id')
        shift_id = request.POST.get('shift_id')
        machine_id = request.POST.get('machine_id')
        component_id = request.POST.get('component_id')
        component_lot_number = request.POST.get('component_lot_number')
        component_quantity = request.POST.get('component_quantity')
        try:
            print("Laser Production Updation Initiated")
            laser_production_obj = models.Laser_production.objects.get(main_id=main_id)
            print(laser_production_obj)
            shift_obj = models.Shifts.objects.get(shift_code=shift_id)
            machine_obj = models.Machines.objects.get(machine_number=machine_id)
            component_obj = models.Components.objects.get(component_type=component_id)
            laser_production_obj.employee_id = employee_id
            laser_production_obj.shift_id = shift_obj
            laser_production_obj.machine_id = machine_obj
            laser_production_obj.component_id = component_obj
            laser_production_obj.component_lot_number = component_lot_number
            laser_production_obj.component_quantity = component_quantity
            laser_production_obj.created_at = datetime.now()
            laser_production_obj.updated_at = datetime.now()
            laser_production_obj.save()
            messages.success(request,"Successfully Updated Laser Production !")
            return HttpResponseRedirect(reverse("operator_laser_production"))
        except:
            messages.error(request,"Failed to Update Laser Production")
            return HttpResponseRedirect(reverse("operator_laser_production"))

def render_delete_laser_production(request, main_id):
    if request.user.is_anonymous:
        return redirect("/")
    else:
        laser_production_obj = models.Laser_production.objects.get(main_id = main_id)
        context = {'laser_production' : laser_production_obj, 'laser_production_id' : main_id}
        print(laser_production_obj)
        return render(request,"bosch_production_app/operator_templates/delete_laser_production.html",context)

def delete_laser_production(request):
    if request.method!="POST":
        return HttpResponse("<h2>Method Not Allowed</h2>")
    else:
        main_id = request.POST.get('main_id')
        try:
            laser_production_obj = models.Laser_production.objects.get(main_id=main_id)
            laser_production_obj.delete()
            messages.success(request,"Successfully Deleted Laser Production !")
            return HttpResponseRedirect(reverse("operator_laser_production"))
        except:
            messages.error(request,"Failed to Delete Laser Production !")
            return HttpResponseRedirect(reverse("operator_laser_production"))

def render_internal_grinding(request):
    if request.user.is_anonymous:
        return redirect("/")
    else:
        return render(request, 'bosch_production_app/operator_templates/internal_grinding.html')

def render_external_grinding(request):
    if request.user.is_anonymous:
        return redirect("/")
    else:
        return render(request, 'bosch_production_app/operator_templates/external_grinding.html')

def render_chamfer_grinding(request):
    if request.user.is_anonymous:
        return redirect("/")
    else:
        return render(request, 'bosch_production_app/operator_templates/chamfer_grinding.html')

def render_aqueous_cleaning(request):
    if request.user.is_anonymous:
        return redirect("/")
    else:
        return render(request, 'bosch_production_app/operator_templates/aqueous_cleaning.html')

def render_operator_profile(request):
    if request.user.is_anonymous:
        return redirect("/")
    else:
        return render(request, 'bosch_production_app/operator_templates/operator_profile.html')
