from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from . import models
from datetime import datetime
from django.contrib import messages
from django.urls import reverse

# Create your views here.

# Creating a rendering function which will render the admin home page for BPS Master
def render_admin_home(request):
    return render(request, 'bosch_production_app/admin_templates/admin_home.html')

def render_dashboard(request):
    return render(request, 'bosch_production_app/admin_templates/dashboard.html')

def render_departments(request):
    department_objs = models.Department.objects.all()
    params = {
        'departments':department_objs
    }
    return render(request, 'bosch_production_app/admin_templates/departments.html', params)

def register_departments(request):
    if request.method != "POST":
        return HttpResponse("Method not Allowed")
    else:
        department_name = request.POST.get("department_name")
        department_desc = request.POST.get("department_desc")
        department_obj = models.Department(department_name=department_name, department_desc=department_desc, created_at=datetime.now(), updated_at=datetime.now())
        department_obj.save()
        messages.success(request, "Department Registered Sucessfully !")
        return HttpResponseRedirect(reverse('departments'))

def render_edit_departments(request, main_id):
    department_obj = models.Department.objects.get(main_id = main_id)
    context = {'departments' : department_obj, 'department_id' : main_id}
    print(department_obj)
    return render(request,"bosch_production_app/admin_templates/edit_departments.html",context)

def edit_departments(request):
    if request.method!="POST":
        return HttpResponse("<h2>Method Not Allowed</h2>")
    else:
        main_id = request.POST.get('department_id')
        department_name = request.POST.get('department_name')
        department_desc = request.POST.get("department_desc")
        try:
            department_obj = models.Department.objects.get(main_id=main_id)
            department_obj.department_name = department_name
            department_obj.department_desc = department_desc
            department_obj.created_at = datetime.now()
            department_obj.updated_at = datetime.now()
            department_obj.save()
            messages.success(request,"Successfully Updated Department !")
            return HttpResponseRedirect(reverse("departments"))
        except:
            messages.error(request,"Failed to Update Department")
            return HttpResponseRedirect("/")

def render_delete_departments(request, main_id):
    department_obj = models.Department.objects.get(main_id = main_id)
    context = {'departments' : department_obj, 'department_id' : main_id}
    print(department_obj)
    return render(request,"bosch_production_app/admin_templates/delete_departments.html",context)

def delete_departments(request):
    if request.method!="POST":
        return HttpResponse("<h2>Method Not Allowed</h2>")
    else:
        main_id = request.POST.get('department_id')
        try:
            department_obj = models.Department.objects.get(main_id=main_id)
            department_obj.delete()
            messages.success(request,"Successfully Deleted Department !")
            return HttpResponseRedirect(reverse("departments"))
        except:
            messages.error(request,"Failed to Delete Department !")
            return HttpResponseRedirect(reverse("departments"))

def render_employees(request):
    department_objs = models.Department.objects.all()
    params = {
        'departments': department_objs
    }
    return render(request, 'bosch_production_app/admin_templates/employees.html', params)

def register_employees(request):
    firstname = request.POST.get("firstname")
    lastname = request.POST.get("lastname")
    username = request.POST.get("username")
    email = request.POST.get("firstname")
    password = request.POST.get("password")
    mobile_no = request.POST.get("mobile_no")
    user_type = request.POST.get("user_type")
    department_id = request.POST.get("department_id")
    try:
        if user_type == "manager":
            user_obj = models.CustomUser.objects.create_user(username=username, password=password, email=email, first_name=firstname, last_name=lastname, user_type=2)
            user_obj.manager.department = models.Department.objects.get(main_id=department_id)
            user_obj.manager.mobile_no = mobile_no
            user_obj.save()
            print("Manager Created")
            messages.success(request, "Manager Registered Sucessfully !")
        if user_type == "expert":
            user_obj = models.CustomUser.objects.create_user(username=username, password=password, email=email, first_name=firstname, last_name=lastname, user_type=3)
            user_obj.expert.department = models.Department.objects.get(main_id=department_id)
            user_obj.expert.mobile_no = mobile_no
            user_obj.save()
            print("expert Created")
            messages.success(request, "Expert Registered Sucessfully !")
        if user_type == "operator":
            user_obj = models.CustomUser.objects.create_user(username=username, password=password, email=email, first_name=firstname, last_name=lastname, user_type=4)
            user_obj.operator.department = models.Department.objects.get(main_id=department_id)
            user_obj.operator.mobile_no = mobile_no
            user_obj.save()
            print("operator Created")
            messages.success(request, "Operator Registered Sucessfully !")
        return HttpResponseRedirect(reverse("employees"))
    except:
        messages.error(request, "Failed to Register Employee")
        return HttpResponseRedirect(reverse("employees"))

def render_components(request):
    component_objs = models.Components.objects.all()
    params = {
        'components':component_objs
    }
    return render(request, 'bosch_production_app/admin_templates/components.html', params)

def register_components(request):
    if request.method != 'POST':
        return HttpResponse('Method not allowed')
    else:
        component_type = request.POST.get('component_type')
        component_lk_number = request.POST.get('component_lk_number')
        component_obj = models.Components(component_type=component_type, component_lk_number=component_lk_number,created_at=datetime.now(),updated_at=datetime.now())
        component_obj.save()
        messages.success(request,"Component Registered Successfully !")
        return HttpResponseRedirect(reverse('components'))

def render_edit_components(request, main_id):
    component_obj = models.Components.objects.get(main_id = main_id)
    context = {'components' : component_obj, 'component_id' : main_id}
    print(component_obj)
    return render(request,"bosch_production_app/admin_templates/edit_components.html",context)

def edit_components(request):
    if request.method!="POST":
        return HttpResponse("<h2>Method Not Allowed</h2>")
    else:
        main_id = request.POST.get('component_id')
        component_type = request.POST.get('component_type')
        component_lk_number = request.POST.get('component_lk_number')
        try:
            component_obj = models.Components.objects.get(main_id=main_id)
            component_obj.component_type = component_type
            component_obj.component_lk_number = component_lk_number
            component_obj.created_at = datetime.now()
            component_obj.updated_at = datetime.now()
            component_obj.save()
            messages.success(request,"Successfully Updated Component !")
            return HttpResponseRedirect(reverse("components"))
        except:
            messages.error(request,"Failed to Update Department")
            return HttpResponseRedirect("/")

def render_delete_components(request, main_id):
    component_obj = models.Components.objects.get(main_id = main_id)
    context = {'components' : component_obj, 'component_id' : main_id}
    print(component_obj)
    return render(request,"bosch_production_app/admin_templates/delete_components.html",context)

def delete_components(request):
    if request.method!="POST":
        return HttpResponse("<h2>Method Not Allowed</h2>")
    else:
        main_id = request.POST.get('component_id')
        try:
            component_obj = models.Components.objects.get(main_id=main_id)
            component_obj.delete()
            messages.success(request,"Successfully Deleted Component !")
            return HttpResponseRedirect(reverse("components"))
        except:
            messages.error(request,"Failed to Delete Component !")
            return HttpResponseRedirect(reverse("components"))

def render_shifts(request):
    shift_objs = models.Shifts.objects.all()
    params = {
        'shifts':shift_objs
    }
    return render(request, 'bosch_production_app/admin_templates/shifts.html', params)

def register_shifts(request):
    if request.method != 'POST':
        return HttpResponse('Method not allowed')
    else:
        shift_code = request.POST.get('shift_code')
        shift_name = request.POST.get('shift_name')
        shift_obj = models.Shifts(shift_code=shift_code, shift_name=shift_name,created_at=datetime.now(),updated_at=datetime.now())
        shift_obj.save()
        messages.success(request,"Shift Registered Successfully !")
        return HttpResponseRedirect(reverse('shifts'))

def render_edit_shifts(request, main_id):
    shift_obj = models.Shifts.objects.get(main_id = main_id)
    context = {'shifts' : shift_obj, 'shift_id' : main_id}
    print(shift_obj)
    return render(request,"bosch_production_app/admin_templates/edit_shifts.html",context)

def edit_shifts(request):
    if request.method!="POST":
        return HttpResponse("<h2>Method Not Allowed</h2>")
    else:
        main_id = request.POST.get('shift_id')
        shift_code = request.POST.get('shift_code')
        shift_name = request.POST.get('shift_name')
        try:
            shift_obj = models.Shifts.objects.get(main_id=main_id)
            shift_obj.shift_code = shift_code
            shift_obj.shift_name = shift_name
            shift_obj.created_at = datetime.now()
            shift_obj.updated_at = datetime.now()
            shift_obj.save()
            messages.success(request,"Successfully Updated Shift !")
            return HttpResponseRedirect(reverse("shifts"))
        except:
            messages.error(request,"Failed to Update Shift")
            return HttpResponseRedirect("/")

def render_delete_shifts(request, main_id):
    shift_obj = models.Shifts.objects.get(main_id = main_id)
    context = {'shifts' : shift_obj, 'shift_id' : main_id}
    print(shift_obj)
    return render(request,"bosch_production_app/admin_templates/delete_shifts.html",context)

def delete_shifts(request):
    if request.method!="POST":
        return HttpResponse("<h2>Method Not Allowed</h2>")
    else:
        main_id = request.POST.get('shift_id')
        try:
            shift_obj = models.Shifts.objects.get(main_id=main_id)
            shift_obj.delete()
            messages.success(request,"Successfully Deleted Shift !")
            return HttpResponseRedirect(reverse("shifts"))
        except:
            messages.error(request,"Failed to Delete Shift !")
            return HttpResponseRedirect(reverse("shifts"))

def render_operations(request):
    operation_objs = models.Operations.objects.all()
    params = {
        'operations':operation_objs
    }
    return render(request, 'bosch_production_app/admin_templates/operations.html', params)

def register_operations(request):
    if request.method != "POST":
        return HttpResponse("Method not Allowed")
    else:
        operation_name = request.POST.get("operation_name")
        operation_obj = models.Operations(operation_name=operation_name, created_at=datetime.now(), updated_at=datetime.now())
        operation_obj.save()
        messages.success(request, "Operation Registered Sucessfully !")
        return HttpResponseRedirect(reverse('operations'))

def render_edit_operations(request, main_id):
    operation_obj = models.Operations.objects.get(main_id = main_id)
    context = {'operations' : operation_obj, 'operation_id' : main_id}
    print(operation_obj)
    return render(request,"bosch_production_app/admin_templates/edit_operations.html",context)

def edit_operations(request):
    if request.method!="POST":
        return HttpResponse("<h2>Method Not Allowed</h2>")
    else:
        main_id = request.POST.get('operation_id')
        operation_name = request.POST.get('operation_name')
        try:
            operation_obj = models.Operations.objects.get(main_id=main_id)
            operation_obj.operation_name = operation_name
            operation_obj.created_at = datetime.now()
            operation_obj.updated_at = datetime.now()
            operation_obj.save()
            messages.success(request,"Successfully Updated Operation !")
            return HttpResponseRedirect(reverse("operations"))
        except:
            messages.error(request,"Failed to Update Operation")
            return HttpResponseRedirect("/")

def render_delete_operations(request, main_id):
    operation_obj = models.Operations.objects.get(main_id = main_id)
    context = {'operations' : operation_obj, 'operation_id' : main_id}
    print(operation_obj)
    return render(request,"bosch_production_app/admin_templates/delete_operations.html",context)

def delete_operations(request):
    if request.method!="POST":
        return HttpResponse("<h2>Method Not Allowed</h2>")
    else:
        main_id = request.POST.get('operation_id')
        try:
            operation_obj = models.Operations.objects.get(main_id=main_id)
            operation_obj.delete()
            messages.success(request,"Successfully Deleted Operation !")
            return HttpResponseRedirect(reverse("operations"))
        except:
            messages.error(request,"Failed to Delete Operation !")
            return HttpResponseRedirect(reverse("operations"))

def render_machines(request):
    machine_objs = models.Machines.objects.all()
    operation_objs = models.Operations.objects.all()
    params = {
        'machines': machine_objs,
        'operations': operation_objs
    }
    return render(request, 'bosch_production_app/admin_templates/machines.html', params)

def register_machines(request):
    if request.method != "POST":
        return HttpResponse("Method not Allowed")
    else:
        machine_number = request.POST.get("machine_number")
        machine_description = request.POST.get("machine_description")
        operation_id = request.POST.get("operation_id")
        operation_obj = models.Operations.objects.get(main_id = operation_id)
        machine_obj = models.Machines(machine_number=machine_number, machine_description=machine_description, operation_id=operation_obj, created_at=datetime.now(), updated_at=datetime.now())
        machine_obj.save()
        messages.success(request, "Machine Registered Sucessfully !")
        return HttpResponseRedirect(reverse('machines'))

def render_edit_machines(request, main_id):
    machine_obj = models.Machines.objects.get(main_id = main_id)
    context = {'machines' : machine_obj, 'machine_id' : main_id}
    print(machine_obj)
    return render(request,"bosch_production_app/admin_templates/edit_machines.html",context)

def edit_machines(request):
    if request.method!="POST":
        return HttpResponse("<h2>Method Not Allowed</h2>")
    else:
        main_id = request.POST.get('machine_id')
        machine_number = request.POST.get('machine_number')
        machine_description = request.POST.get('machine_description')
        operation_id = request.POST.get('operation_id')
        try:
            machine_obj = models.Machines.objects.get(main_id=main_id)
            operation_obj = models.Operations.objects.get(operation_name=operation_id)
            machine_obj.machine_number = machine_number
            machine_obj.machine_description = machine_description
            machine_obj.operation_id = operation_obj
            machine_obj.created_at = datetime.now()
            machine_obj.updated_at = datetime.now()
            machine_obj.save()
            messages.success(request,"Successfully Updated Machine !")
            return HttpResponseRedirect(reverse("machines"))
        except:
            messages.error(request,"Failed to Update Machine")
            return HttpResponseRedirect("/")

def render_delete_machines(request, main_id):
    machine_obj = models.Machines.objects.get(main_id = main_id)
    context = {'machines' : machine_obj, 'machine_id' : main_id}
    print(machine_obj)
    return render(request,"bosch_production_app/admin_templates/delete_machines.html",context)

def delete_machines(request):
    if request.method!="POST":
        return HttpResponse("<h2>Method Not Allowed</h2>")
    else:
        main_id = request.POST.get('machine_id')
        try:
            machine_obj = models.Machines.objects.get(main_id=main_id)
            machine_obj.delete()
            messages.success(request,"Successfully Deleted Machine !")
            return HttpResponseRedirect(reverse("machines"))
        except:
            messages.error(request,"Failed to Delete Machine !")
            return HttpResponseRedirect(reverse("machines"))

def render_laser_production(request):
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
    return render(request, 'bosch_production_app/admin_templates/laser_production.html', params)

def register_laser_production(request):
    if request.method != "POST":
        return HttpResponse("Method not Allowed")
    else:
        Laser_production_obj = models.Laser_production.objects.create(employee_id = request.POST.get("employee_id"), shift_id = models.Shifts.objects.get(main_id = request.POST.get("shift_code")), machine_id = models.Machines.objects.get(main_id=request.POST.get("machine_number")), component_id = models.Components.objects.get(main_id = request.POST.get("component_type")), component_lot_number = request.POST.get("component_lot_number"), component_quantity = request.POST.get("component_quantity"), created_at=datetime.now(), updated_at=datetime.now())
        Laser_production_obj.save()
        messages.success(request, "Laser Production Registered Sucessfully !")
        return HttpResponseRedirect(reverse('laser_production'))

def render_edit_laser_production(request, main_id):
    laser_production_obj = models.Laser_production.objects.get(main_id = main_id)
    context = {'laser_production' : laser_production_obj, 'laser_production_id' : main_id}
    print(laser_production_obj)
    return render(request,"bosch_production_app/admin_templates/edit_laser_production.html",context)

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
            return HttpResponseRedirect(reverse("laser_production"))
        except:
            messages.error(request,"Failed to Update Laser Production")
            return HttpResponseRedirect(reverse("laser_production"))

def render_delete_laser_production(request, main_id):
    laser_production_obj = models.Laser_production.objects.get(main_id = main_id)
    context = {'laser_production' : laser_production_obj, 'laser_production_id' : main_id}
    print(laser_production_obj)
    return render(request,"bosch_production_app/admin_templates/delete_laser_production.html",context)

def delete_laser_production(request):
    if request.method!="POST":
        return HttpResponse("<h2>Method Not Allowed</h2>")
    else:
        main_id = request.POST.get('main_id')
        try:
            laser_production_obj = models.Laser_production.objects.get(main_id=main_id)
            laser_production_obj.delete()
            messages.success(request,"Successfully Deleted Laser Production !")
            return HttpResponseRedirect(reverse("laser_production"))
        except:
            messages.error(request,"Failed to Delete Laser Production !")
            return HttpResponseRedirect(reverse("laser_production"))
