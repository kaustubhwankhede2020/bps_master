from django.contrib import admin
from . import models

# Register your models here.
admin.site.register(models.CustomUser)
admin.site.register(models.Department)
admin.site.register(models.Admin)
admin.site.register(models.Manager)
admin.site.register(models.Expert)
admin.site.register(models.Operator)
admin.site.register(models.Components)
admin.site.register(models.Shifts)
admin.site.register(models.Operations)
admin.site.register(models.Machines)
admin.site.register(models.Laser_production)