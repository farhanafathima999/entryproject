# Generated by Django 4.2.4 on 2024-01-27 15:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hospital_app', '0005_delete_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='appointment',
            name='doctor_profile_pic',
            field=models.ImageField(blank=True, null=True, upload_to='profile_pic'),
        ),
        migrations.AddField(
            model_name='appointment',
            name='patient_profile_pic',
            field=models.ImageField(blank=True, null=True, upload_to='profile_pic'),
        ),
    ]
