# Generated by Django 5.0.6 on 2024-05-31 11:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exercise', '0002_rename_details_detail'),
    ]

    operations = [
        migrations.AlterField(
            model_name='detail',
            name='exercisesteps',
            field=models.TextField(max_length=10000),
        ),
    ]
