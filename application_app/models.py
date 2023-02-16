from django.db import models
from Admin_app.models import Users

MARITAL_STATUS = [('Married','Married'), ('Unmarried', 'Unmarried'), ('Divorse', 'Divorse')]
EMPLOYMENT_CHOICE = [('Self_employed','Self_employed'), ('Private', 'Private')]
BUSINESS_TYPE = [('Sole','Sole'), ('Partnership','Partnership'), ('Corporation','Corporation')]
APPLICATION_STATUS = [('Inprocess','Inprocess'), ('Approved', 'Approved'), ('Rejected', 'Rejected')]
GENDER_CHOICES = [('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')]
BUSINESS_constitution = [('Private_limited','Private_limited'), ('Public_limited','Public_limited'), ('Partnership','Partnership'), ('One_person_companies','One_person_companies')]



# Create your models here.

class Family(models.Model):
    user = models.OneToOneField(Users, on_delete=models.CASCADE, related_name='Familys')
    father_name = models.CharField(max_length=250, default=0, blank=True)
    father_profession = models.CharField(max_length=250, default=0, blank=True)
    mother_name = models.CharField(max_length=250, default=0, blank=True)
    mother_profession = models.CharField(max_length=250, default=0, blank=True)
    marital_status = models.CharField(max_length=250, choices=MARITAL_STATUS, default=0, blank=True)
    spouse_name = models.CharField(max_length=250, default=0, blank=True)
    spouse_profession = models.CharField(max_length=250, default=0, blank=True)
    mobile = models.CharField(max_length=10, default=0, blank=True)
    address = models.TextField(default=0, blank=True)

    def __str__(self):
        return f"{self.id}"


class Application(models.Model): 
    user = models.ForeignKey(Users, on_delete=models.CASCADE, related_name='Applications')
    aadhaar_no = models.CharField(max_length=12, default=0, blank=True)
    pan_no = models.CharField(max_length=10, default=0, blank=True)
    type_of_employment = models.CharField(max_length=250, choices=EMPLOYMENT_CHOICE, default=0, blank=True)
    business_title = models.CharField(max_length=250, default=0, blank=True)
    business_type = models.CharField(max_length=250, choices=BUSINESS_TYPE, default=0, blank=True)
    business_address = models.TextField(default=0, blank=True)
    gst_registration_no = models.CharField(max_length=50, default=0, blank=True)
    business_license_no = models.CharField(max_length=50, default=0, blank=True)
    expected_average_annual_turnover = models.CharField(max_length=250, default=0, blank=True)
    years_in_current_business = models.IntegerField(default=0, blank=True)
    collateral = models.CharField(max_length=250, default=0, blank=True)
    status = models.CharField(max_length=250, default='', choices=APPLICATION_STATUS)
    application_timestamp = models.DateTimeField(auto_now_add=True, blank=True)
    remark = models.CharField(max_length=250, default=0, blank=True)

    def __str__(self):
        return f"{self.id}, {self.user}, {self.aadhaar_no}"

    

class Guarantor(models.Model):
    application = models.ForeignKey(Application, on_delete=models.CASCADE, related_name='Guarantors')
    relation_with_customer = models.CharField(max_length=250, default=0, blank=True)
    name = models.CharField(max_length=150, default=0, blank=True)
    dob = models.DateField(default="2000-12-12", blank=True)
    gender = models.CharField(max_length=50,  default=0, blank=True, choices=GENDER_CHOICES)
    email = models.EmailField(default=0, blank=True)
    address = models.TextField(max_length=250, default=0, blank=True)
    city = models.CharField(max_length=50, default=0,blank=True)
    state = models.CharField(max_length=50, default=0,blank=True)
    country = models.CharField(max_length=250, default=0, blank=True)
    pin_code = models.IntegerField(default=0, blank=True)
    mobile = models.CharField(max_length=10,default=0, blank=True)
    photo = models.ImageField(upload_to='media/customer/guarantor/', default=0, blank=True)
    profession = models.CharField(max_length=250, default=0, blank=True)
    income_certificate = models.FileField(upload_to='media/customer/guarantor/', default=0, blank=True)
    bank_name = models.CharField(max_length=250, default=0, blank=True)
    current_account_no = models.CharField(max_length=20, default=0, blank=True)
    passbook_copy = models.FileField(upload_to='media/customer/guarantor/', default=0, blank=True)
    ifsc_code = models.CharField(max_length=20, default=0, blank=True)

    def __str__(self):
       	return f'{self.id}'



class Business(models.Model):
    loan = models.OneToOneField(Application, on_delete=models.CASCADE, related_name='Business')
    business_title = models.CharField(max_length=250, default=0, blank=True)
    email = models.EmailField(default=0, blank=True)
    contact_details_1 = models.CharField(max_length=15)
    contact_details_2 = models.CharField(max_length=15)
    udyog_aadhar_no = models.CharField(max_length=50, default=0, blank=True)
    gst_registration_no = models.CharField(max_length=50, default=0, blank=True)
    business_license_no = models.CharField(max_length=50, default=0, blank=True)
    pan_card_no = models.CharField(max_length=50, default=0, blank=True)
    date_of_incorporation = models.DateField(blank=True)
    business_type = models.CharField(max_length=250, choices=BUSINESS_TYPE, default=0, blank=True)
    business_constitution = models.CharField(max_length=100, choices=BUSINESS_constitution, default='owner', blank=True)
    business_address = models.TextField(default=0, blank=True)
    CIBIL_score = models.IntegerField(default=0, blank=True)
    past1_year_turnover = models.CharField(max_length=50, default=0, blank=True)
    past2_year_turnover = models.CharField(max_length=50, default=0, blank=True)
    expected_average_annual_turnover = models.CharField(max_length=250, default=0, blank=True)
    years_in_current_business = models.IntegerField(default=0, blank=True)

    def __str__(self):
        return f"{self.id}"