from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from datetime import datetime

# Create your models here.
class CustomUser(AbstractUser):
    user_type_data = ((1, "Admin"),(2, "Manager"),(3, "Expert"),(4, "Operator"))
    user_type = models.CharField(choices=user_type_data, default=1, max_length=10)
    employee_number = models.CharField(max_length=20, default="")

class Admin(models.Model):
    main_id = models.AutoField(primary_key=True)
    user_design = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    mobile_no = models.CharField(max_length=15)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    objects = models.Manager()

class Department(models.Model):
    main_id = models.AutoField(primary_key=True)
    department_name = models.CharField(max_length=20)
    department_desc = models.TextField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    objects = models.Manager()

    def __str__(self):
        return self.department_name

class Manager(models.Model):
    main_id = models.AutoField(primary_key=True)
    department = models.ForeignKey(Department, on_delete=models.DO_NOTHING, default=1)
    user_design = models.OneToOneField(CustomUser, on_delete=models.CASCADE, default=1)
    mobile_no = models.CharField(max_length=15)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    objects = models.Manager()

class Expert(models.Model):
    main_id = models.AutoField(primary_key=True)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    user_design = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    mobile_no = models.CharField(max_length=15)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    objects = models.Manager()

class Operator(models.Model):
    main_id = models.AutoField(primary_key=True)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    user_design = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    mobile_no = models.CharField(max_length=15)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    objects = models.Manager()

class Components(models.Model):
    main_id = models.AutoField(primary_key=True)
    component_type = models.CharField(max_length=25)
    component_lk_number = models.CharField(max_length=25)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    objects = models.Manager()

    def __str__(self):
        return self.component_type
        
class Operations(models.Model):
    main_id = models.AutoField(primary_key=True)
    operation_name = models.CharField(max_length=25)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    objects = models.Manager()
    def __str__(self):
        return self.operation_name

class Machines(models.Model):
    main_id = models.AutoField(primary_key=True)
    machine_number = models.CharField(max_length=12)
    machine_description = models.CharField(max_length=25)
    operation_id = models.ForeignKey(Operations, on_delete=models.CASCADE)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    objects = models.Manager()

    def __str__(self):
        return self.machine_number

class Shifts(models.Model):
    main_id = models.AutoField(primary_key=True)
    shift_code = models.CharField(max_length=5)
    shift_name = models.CharField(max_length=10)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    objects = models.Manager()

    def __str__(self):
        return self.shift_code

class Laser_production(models.Model):
    main_id = models.AutoField(primary_key=True)
    employee_id = models.CharField(max_length=10)
    shift_id = models.ForeignKey(Shifts, on_delete=models.CASCADE)
    machine_id = models.ForeignKey(Machines, on_delete=models.CASCADE)
    component_id = models.ForeignKey(Components, on_delete=models.CASCADE)
    component_lot_number = models.CharField(max_length=5)
    component_quantity = models.CharField(max_length=5)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    objects = models.Manager()

@receiver(post_save,sender=CustomUser)
def create_user_profile(sender,instance,created,**kwargs):
    if created:
        if instance.user_type==1:
            Admin.objects.create(user_design=instance, mobile_no="", created_at=datetime.now(), updated_at=datetime.now())
        if instance.user_type==2:
            Manager.objects.create(user_design=instance,department=Department.objects.get(main_id=1), mobile_no="", created_at=datetime.now(), updated_at=datetime.now())
        if instance.user_type==3:
            Expert.objects.create(user_design=instance,department=Department.objects.get(main_id=1), mobile_no="", created_at=datetime.now(), updated_at=datetime.now())
        if instance.user_type==4:
            Operator.objects.create(user_design=instance,department=Department.objects.get(main_id=1), mobile_no="", created_at=datetime.now(), updated_at=datetime.now())

@receiver(post_save,sender=CustomUser)
def save_user_profile(sender,instance,**kwargs):
    if instance.user_type==1:
        instance.admin.save()
    if instance.user_type==2:
        instance.manager.save()
    if instance.user_type==3:
        instance.expert.save()
    if instance.user_type==4:
        instance.operator.save()
