# Generated by Django 4.1.3 on 2023-02-10 10:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Admin_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='gender',
            field=models.CharField(choices=[('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')], max_length=50),
        ),
        migrations.AlterField(
            model_name='users',
            name='role',
            field=models.CharField(choices=[('Customer', 'Customer'), ('Loan Representative', 'Loan Representative'), ('Operational Head', 'Operational Head'), ('Loan Sanction Officer', 'Loan Sanction Officer'), ('Admin', 'Admin')], default='customer', max_length=50),
        ),
    ]
