# Generated by Django 4.2.2 on 2023-06-25 20:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='is_superadmin',
            field=models.BooleanField(default=False),
        ),
    ]
