from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
import os

# Create your models here.
class Degsif18Y3010919(models.Model):
    uid = models.CharField(max_length=36, blank=True, null=True)
    mid = models.CharField(max_length=96, blank=True, null=True)
    reg_no = models.CharField(max_length=33, blank=True, null=True)
    exm_roll = models.CharField(max_length=21, blank=True, null=True)
    std_name = models.CharField(max_length=180, blank=True, null=True)
    fname = models.CharField(max_length=180, blank=True, null=True)
    mname = models.CharField(max_length=180, blank=True, null=True)
    c_code = models.CharField(max_length=9, blank=True, null=True)
    centre = models.CharField(max_length=240, blank=True, null=True)
    issu_date = models.CharField(max_length=36, blank=True, null=True)
    old_col = models.CharField(max_length=240, blank=True, null=True)
    col_code = models.CharField(max_length=12, blank=True, null=True)
    college = models.CharField(max_length=240, blank=True, null=True)
    sub_code = models.CharField(max_length=3, blank=True, null=True)
    sess = models.CharField(max_length=30, blank=True, null=True)
    sif = models.CharField(max_length=240, blank=True, null=True)
    opt_all = models.CharField(max_length=120, blank=True, null=True)
    opt_all_ne = models.CharField(max_length=90, blank=True, null=True)
    opt_all_ol = models.CharField(max_length=90, blank=True, null=True)
    session = models.CharField(max_length=36, blank=True, null=True)
    std_type = models.CharField(max_length=3, blank=True, null=True)
    course = models.CharField(max_length=3, blank=True, null=True)
    course_nam = models.CharField(max_length=60, blank=True, null=True)
    adm_roll = models.CharField(max_length=21, blank=True, null=True)
    abs_sub = models.CharField(max_length=180, blank=True, null=True)
    exm_fee = models.CharField(max_length=21, blank=True, null=True)
    year = models.CharField(max_length=36, blank=True, null=True)
    sdate = models.CharField(max_length=36, blank=True, null=True)
    confirm_da = models.CharField(max_length=36, blank=True, null=True)
    status = models.CharField(max_length=30, blank=True, null=True)
    complete = models.CharField(max_length=30, blank=True, null=True)
    std_status = models.CharField(max_length=90, blank=True, null=True)
    imp_all = models.CharField(max_length=240, blank=True, null=True)
    syll = models.CharField(max_length=90, blank=True, null=True)
    syll_yr = models.CharField(max_length=90, blank=True, null=True)
    confirm_d1 = models.CharField(max_length=90, blank=True, null=True)
    sif_sub = models.CharField(max_length=120, blank=True, null=True)
    pic_sessio = models.CharField(max_length=12, blank=True, null=True)
    session_ty = models.CharField(max_length=20, blank=True, null=True)
    admission_field = models.CharField(db_column='admission_', max_length=10, blank=True, null=True)  # Field renamed because it ended with '_'.
    id = models.BigAutoField(db_column='ID', primary_key=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'degsif18y3010919'

class Student(models.Model):
    reg_no = models.CharField(max_length=20, unique=True)
    std_name = models.CharField(max_length=100)
    fname = models.CharField(max_length=100)
    mname = models.CharField(max_length=100)
    gender = models.CharField(max_length=10)  # For additional data
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    username = models.CharField(max_length=50)
    date_of_birth = models.DateField()
    marital_status = models.CharField(max_length=50)
    nationality = models.CharField(max_length=30)
    spouse_name = models.CharField(max_length=100, blank=True)
    number_of_children = models.IntegerField(default=0)
    picture = models.ImageField(upload_to='member_images', blank=True)
     # Completion Status
    personal_info_complete = models.BooleanField(default=False)
    contact_info_complete = models.BooleanField(default=False)
    professional_info_complete = models.BooleanField(default=False)
    payment_info_complete = models.BooleanField(default=False)

    def __str__(self):
        return self.std_name

    def save(self, *args, **kwargs):
        # Call the original save method to save the instance first
        super().save(*args, **kwargs)

        # Rename the image file after saving the instance
        if self.picture:
            # Get the file extension
            ext = os.path.splitext(self.picture.name)[1]
            # Create the new filename using reg_no
            new_filename = f"{self.reg_no}{ext}"
            # Construct the full path for the new file
            new_file_path = os.path.join(self.picture.storage.location,'member_images', new_filename)

            # Rename the file
            os.rename(self.picture.path, new_file_path)

            # Update the picture field with the new filename
            self.picture.name = f'member_images/{new_filename}'
            super().save(update_fields=['picture'])  # Save the updated picture field

class AddressJob(models.Model):
    # Contact Information
    present_address = models.TextField()
    present_dist = models.TextField()
    present_upozilla = models.TextField()
    permanent_address = models.TextField()
    permanent_dist= models.TextField()
    permanent_upozilla = models.TextField()
    
    work_address = models.TextField()
    work_dist= models.TextField()
    work_upozilla= models.TextField()
    company_name= models.TextField(max_length=50, null=True)
    occupation = models.CharField(max_length=100, null=True)
    designation = models.CharField(max_length=100, null=True)
    mobile = models.CharField(max_length=11, null=False, blank=False, default='00000000000')
    telephone = models.CharField(max_length=14, null=True)
    highest_degree_obtained = models.TextField(null=True)
    category_of_membership = models.CharField(max_length=100,null=True)
    amount_payable = models.DecimalField(max_digits=10, decimal_places=2,null=True) 
    
    def __str__(self):
        return self.present_address   


class District(models.Model):
    district = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'district'


class Upozilla(models.Model):
    district = models.CharField(max_length=255, blank=True, null=True)
    upozilla = models.CharField(max_length=255, blank=True, null=True)
    dist_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'upozilla'   

    '''class Student(models.Model):
    reg_no = models.CharField(max_length=20, unique=True)
    std_name = models.CharField(max_length=100)
    fname = models.CharField(max_length=100)
    mname = models.CharField(max_length=100)
    gender = models.CharField(max_length=10)  # For additional data
    #user= models.ForeignKey(User, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    #user= models.CharField(settings.AUTH_USER_MODEL,max_length=10)
    username = models.CharField(max_length=50)
   

    def __str__(self):
        return self.std_name
    
class Member(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    
    # Personal Information
    name = models.CharField(max_length=100)
    date_of_birth = models.DateField()

    gender = models.CharField(max_length=20)
    marital_status = models.CharField(max_length=50)

    nationality = models.CharField(max_length=30)
    spouse_name = models.CharField(max_length=100, blank=True)
    number_of_children = models.IntegerField(default=0)
    picture = models.ImageField(upload_to='Images/Member', blank=True)
     
    
    # Contact Information
    present_address = models.TextField()
    permanent_address = models.TextField()
    phone_mobile = models.CharField(max_length=14)
    phone_telephone = models.CharField(max_length=14, blank=True)
    email_address = models.EmailField()
    highest_degree_obtained = models.TextField()  # Could be a separate model if you need more structure
    
    # Professional Information
    occupation = models.CharField(max_length=100)
    designation = models.CharField(max_length=100)
    work_address = models.TextField()
    category_of_membership = models.CharField(max_length=100)
    amount_payable_for_membership = models.DecimalField(max_digits=10, decimal_places=2)
    
    # Payment Information

    mode_of_payment = models.CharField(max_length=20)
    specific_payment_option = models.CharField(max_length=50, blank=True, null=True)

     # Completion Status
    personal_info_complete = models.BooleanField(default=False)
    contact_info_complete = models.BooleanField(default=False)
    professional_info_complete = models.BooleanField(default=False)
    payment_info_complete = models.BooleanField(default=False)
    
    def __str__(self):
        return self.name
    
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    ]
    NATIONALITY_CHOICES = [
        ('B', 'Bangladeshi'),
        ('O', 'Non Bangladeshi'),
    ]
    MODE_OF_PAYMENT_CHOICES = [
        ('MB', 'Mobile Banking'),
        ('BT', 'Bank Transfer'),
    ]'''

 