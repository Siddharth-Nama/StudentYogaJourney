# Generated by Django 5.0.6 on 2024-06-14 13:13

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RenameField(
            model_name='customuser',
            old_name='Dob',
            new_name='dob',
        ),
        migrations.AlterField(
            model_name='customuser',
            name='phone',
            field=models.CharField(default='+91987654321', max_length=15),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='customuser', to=settings.AUTH_USER_MODEL),
        ),
    ]