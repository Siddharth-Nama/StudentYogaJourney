# Generated by Django 5.0.6 on 2024-05-27 10:47

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(default='example@gmail.com', max_length=254)),
                ('phone', models.CharField(default='987654321', max_length=15)),
                ('Dob', models.DateField(default='2004-04-26')),
                ('image', models.ImageField(upload_to='profile')),
                ('user', models.OneToOneField(default='sidd', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
