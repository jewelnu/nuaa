# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Admit24(models.Model):
    reg_no = models.BigIntegerField(primary_key=True)
    std_name = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'admit24'


class Allcol191(models.Model):
    male = models.CharField(db_column='MALE', max_length=1, blank=True, null=True)  # Field name made lowercase.
    female = models.CharField(db_column='FEMALE', max_length=1, blank=True, null=True)  # Field name made lowercase.
    male_fema = models.CharField(db_column='MALE_FEMA', max_length=1, blank=True, null=True)  # Field name made lowercase.
    divi_name = models.CharField(db_column='DIVI_NAME', max_length=24, blank=True, null=True)  # Field name made lowercase.
    dist_name = models.CharField(db_column='DIST_NAME', max_length=30, blank=True, null=True)  # Field name made lowercase.
    thana_name = models.CharField(db_column='THANA_NAME', max_length=30, blank=True, null=True)  # Field name made lowercase.
    col_code = models.CharField(db_column='COL_CODE', max_length=4, blank=True, null=True)  # Field name made lowercase.
    college = models.CharField(db_column='COLLEGE', max_length=80, blank=True, null=True)  # Field name made lowercase.
    govt_stat = models.CharField(db_column='GOVT_STAT', max_length=1, blank=True, null=True)  # Field name made lowercase.
    eiin = models.CharField(db_column='EIIN', max_length=10, blank=True, null=True)  # Field name made lowercase.
    establish = models.CharField(db_column='ESTABLISH', max_length=10, blank=True, null=True)  # Field name made lowercase.
    status = models.CharField(db_column='STATUS', max_length=35, blank=True, null=True)  # Field name made lowercase.
    comments = models.CharField(db_column='COMMENTS', max_length=2, blank=True, null=True)  # Field name made lowercase.
    email = models.CharField(db_column='EMAIL', max_length=30, blank=True, null=True)  # Field name made lowercase.
    mobile = models.CharField(db_column='MOBILE', max_length=15, blank=True, null=True)  # Field name made lowercase.
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'allcol19_1'


class AlumniContact(models.Model):
    id = models.BigAutoField(primary_key=True)
    email = models.CharField(max_length=254)
    subject = models.CharField(max_length=255)
    message = models.TextField()

    class Meta:
        managed = False
        db_table = 'alumni_contact'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DegreeSubjectNew(models.Model):
    sl_no = models.CharField(max_length=254, blank=True, null=True)
    sub_code1 = models.CharField(max_length=254, blank=True, null=True)
    sub_code = models.CharField(max_length=254, blank=True, null=True)
    pap_code = models.CharField(max_length=254, blank=True, null=True)
    pap_name = models.CharField(max_length=254, blank=True, null=True)
    sub_name = models.CharField(max_length=254, blank=True, null=True)
    sub_title = models.CharField(max_length=254, blank=True, null=True)
    course = models.CharField(max_length=254, blank=True, null=True)
    sub_all = models.CharField(max_length=254, blank=True, null=True)
    sub_1st = models.CharField(max_length=254, blank=True, null=True)
    sub_2nd = models.CharField(max_length=254, blank=True, null=True)
    sub_3rd = models.CharField(max_length=254, blank=True, null=True)
    status = models.CharField(max_length=10, blank=True, null=True)
    opt_all = models.CharField(max_length=60, blank=True, null=True)
    dis_head = models.CharField(max_length=10, blank=True, null=True)
    packet = models.CharField(max_length=10, blank=True, null=True)
    serial = models.CharField(db_column='Serial', max_length=5, blank=True, null=True)  # Field name made lowercase.
    question_s = models.CharField(db_column='Question_s', max_length=10, blank=True, null=True)  # Field name made lowercase.
    pap_order = models.CharField(db_column='Pap_order', max_length=5, blank=True, null=True)  # Field name made lowercase.
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'degree_Subject_New'


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


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class PaymentsPayMethod(models.Model):
    id = models.BigAutoField(primary_key=True)
    pay_id = models.IntegerField()
    pay_option = models.CharField(max_length=50)
    min_pay = models.IntegerField()
    max_payment = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'payments_pay_method'


class ProductCustomertable(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(db_column='Name', max_length=50)  # Field name made lowercase.
    email = models.CharField(db_column='Email', max_length=50)  # Field name made lowercase.
    password = models.CharField(db_column='Password', max_length=50)  # Field name made lowercase.
    reenter_password = models.CharField(db_column='ReEnter_Password', max_length=50)  # Field name made lowercase.
    mobile_number = models.CharField(db_column='Mobile_Number', max_length=50)  # Field name made lowercase.
    second_mobile = models.CharField(db_column='Second_Mobile', max_length=50)  # Field name made lowercase.
    textarea = models.CharField(db_column='TextArea', max_length=50)  # Field name made lowercase.
    checkiftrue = models.CharField(db_column='CheckIfTrue', max_length=5)  # Field name made lowercase.
    rating = models.IntegerField(db_column='Rating')  # Field name made lowercase.
    amount = models.DecimalField(db_column='Amount', max_digits=5, decimal_places=2)  # Field name made lowercase.
    youtube_channel = models.BooleanField(db_column='Youtube_channel')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'product_customertable'


class UserAuthenticationProfile(models.Model):
    id = models.BigAutoField(primary_key=True)
    mobile = models.CharField(max_length=15)
    user = models.OneToOneField(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'user_authentication_profile'
