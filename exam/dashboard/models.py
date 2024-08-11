from django.db import models
from django.contrib.auth.models import User

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
    user= models.ForeignKey(User, on_delete=models.CASCADE)
    username = models.CharField(max_length=50)

    def __str__(self):
        return self.std_name