# Generated by Django 4.2.2 on 2023-10-15 13:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hospitals', '0002_remove_patient_doctor_reservation'),
    ]

    operations = [
        migrations.AddField(
            model_name='patient',
            name='doctors',
            field=models.ManyToManyField(to='hospitals.doctor'),
        ),
    ]
