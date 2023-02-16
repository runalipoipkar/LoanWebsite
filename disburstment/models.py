from django.db import models
from loan_sanctioning.models import Loan
from application_app.models import Application
from django.contrib.auth.models import User

INSTALLMENT_CHOICES = [('Pending', 'pending')]
PAYMENT_CHOICES = [('Cash','Cash'), ('Cheque','Cheque'), ('UPI','UPI')]
DISBURSEMENT_CHOICES = [('In_process','In_process'), ('Pending', 'Pending')]
BUSINESS_TYPE = [('Sole','Sole'), ('Partnership','Partnership'), ('Corporation','Corporation')]
BUSINESS_constitution = [('Private_limited','Private_limited'), ('Public_limited','Public_limited'), ('Partnership','Partnership'), ('One_person_companies','One_person_companies')]

# Create your models here.
class Vendor(models.Model):
    application = models.ForeignKey(Application, on_delete=models.CASCADE, related_name='Vendors')
    name = models.CharField(max_length=250, default=0, blank=True)
    vendor_type = models.CharField(max_length=250, default=0, blank=True)
    email = models.EmailField(default=0, blank=True)
    address = models.TextField(max_length=250, default=0, blank=True)
    city = models.CharField(max_length=250, default=0,blank=True)
    state = models.CharField(max_length=250, default=0, blank=True)
    country = models.CharField(max_length=250, default=0, blank=True)
    pin_code = models.IntegerField(default=0, blank=True)
    mobile = models.CharField(max_length=10,default=0, blank=True)
    bank_name = models.CharField(max_length=250, default=0, blank=True)
    passbook_copy = models.FileField(upload_to='customer/vendor/', default=0, blank=True)
    current_account_no = models.CharField(max_length=25, default=0, blank=True)
    ifsc_code = models.CharField(max_length=20, default=0, blank=True)

    def __str__(self):
        return f"{self.id}"

class Installment(models.Model):
    loan = models.ForeignKey(Loan, on_delete=models.CASCADE, related_name='Installments')
    remaining_amount = models.FloatField(default=0, blank=True)
    installment_no = models.IntegerField(default=0, blank=True)
    monthly_installment_amount = models.FloatField(default=0, blank=True)
    installment_expected_date = models.DateField(default="2000-12-12", blank=True)
    installment_paid_date = models.DateField(default="2000-12-12", blank=True)
    penalty_amount = models.FloatField(default=0, blank=True)
    status = models.CharField(max_length=100, blank=True, choices=INSTALLMENT_CHOICES, default='pending')

    def __str__(self):
       	return f"{self.id}"

class Disbursement(models.Model):
    loan = models.OneToOneField(Loan, on_delete=models.CASCADE, related_name='Disbursements')
    insurance_doc = models.FileField(upload_to='media/customer/disbursement', default=0, blank=True)
    payment_mode = models.CharField(max_length=250, default=0, blank=True, choices=PAYMENT_CHOICES)
    net_disbursed_amount = models.FloatField(default=0, blank=True)
    disbursed_to_account_no = models.CharField(max_length=25, default=0, blank=True)
    receipt_doc = models.FileField(upload_to='customer/disbursement', default=0, blank=True)
    status = models.CharField(max_length=250, default=0, blank=True, choices=DISBURSEMENT_CHOICES)
    response_timestamp = models.DateTimeField(auto_now=True, blank=True)

    def __str__(self):
        return f"{self.id}"