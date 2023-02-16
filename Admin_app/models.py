from django.db import models

from django.contrib.auth.models import AbstractUser


GENDER_CHOICES = [('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')]
ROLE_CHOICES = [('Customer', 'Customer'), ('Loan Representative', 'Loan Representative'), ('Operational Head', 'Operational Head'), ('Loan Sanction Officer', 'Loan Sanction Officer'), ('Admin', 'Admin')]


class Users(AbstractUser):

    first_name = models.CharField(max_length=250)
    last_name = models.CharField(max_length=250)
    dob = models.DateField(default="2000-12-12", blank=True)
    gender = models.CharField(max_length=50, choices=GENDER_CHOICES)
    email = models.EmailField(db_index=True, max_length=50, unique=True)
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=250)
    state = models.CharField(max_length=250)
    country = models.CharField(max_length=250)
    pin_code = models.IntegerField(default=0, blank=True)
    mobile = models.CharField(max_length=10)
    photo = models.ImageField(upload_to="customer/user/", default=0, blank=True)
    signature = models.ImageField(upload_to="customer/user/", default=0, blank=True)
    role = models.CharField(max_length=50, default='customer', choices=ROLE_CHOICES)

    REQUIRED_FIELDS = ['first_name', 'last_name', 'mobile']

    class Meta:
        db_table = 'df_user'
        verbose_name = 'User'
        verbose_name_plural = 'Users'




class Defaulter(models.Model):
    user = models.OneToOneField(Users, on_delete=models.CASCADE, related_name='Defaulters')
    default_amount = models.FloatField(default=0, blank=True)
    pending_since_date = models.DateField(default="2000-12-12", blank=True)
    
    def __str__(self):
        return f"{self.id}"