# Generated by Django 3.1.5 on 2021-02-08 01:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bosch_production_app', '0004_auto_20210208_0625'),
    ]

    operations = [
        migrations.AlterField(
            model_name='manager',
            name='department',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='bosch_production_app.department'),
        ),
    ]
