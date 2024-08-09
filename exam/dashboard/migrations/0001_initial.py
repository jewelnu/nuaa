# Generated by Django 5.0.4 on 2024-08-09 12:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Degsif18Y3010919',
            fields=[
                ('uid', models.CharField(blank=True, max_length=36, null=True)),
                ('mid', models.CharField(blank=True, max_length=96, null=True)),
                ('reg_no', models.CharField(blank=True, max_length=33, null=True)),
                ('exm_roll', models.CharField(blank=True, max_length=21, null=True)),
                ('std_name', models.CharField(blank=True, max_length=180, null=True)),
                ('fname', models.CharField(blank=True, max_length=180, null=True)),
                ('mname', models.CharField(blank=True, max_length=180, null=True)),
                ('c_code', models.CharField(blank=True, max_length=9, null=True)),
                ('centre', models.CharField(blank=True, max_length=240, null=True)),
                ('issu_date', models.CharField(blank=True, max_length=36, null=True)),
                ('old_col', models.CharField(blank=True, max_length=240, null=True)),
                ('col_code', models.CharField(blank=True, max_length=12, null=True)),
                ('college', models.CharField(blank=True, max_length=240, null=True)),
                ('sub_code', models.CharField(blank=True, max_length=3, null=True)),
                ('sess', models.CharField(blank=True, max_length=30, null=True)),
                ('sif', models.CharField(blank=True, max_length=240, null=True)),
                ('opt_all', models.CharField(blank=True, max_length=120, null=True)),
                ('opt_all_ne', models.CharField(blank=True, max_length=90, null=True)),
                ('opt_all_ol', models.CharField(blank=True, max_length=90, null=True)),
                ('session', models.CharField(blank=True, max_length=36, null=True)),
                ('std_type', models.CharField(blank=True, max_length=3, null=True)),
                ('course', models.CharField(blank=True, max_length=3, null=True)),
                ('course_nam', models.CharField(blank=True, max_length=60, null=True)),
                ('adm_roll', models.CharField(blank=True, max_length=21, null=True)),
                ('abs_sub', models.CharField(blank=True, max_length=180, null=True)),
                ('exm_fee', models.CharField(blank=True, max_length=21, null=True)),
                ('year', models.CharField(blank=True, max_length=36, null=True)),
                ('sdate', models.CharField(blank=True, max_length=36, null=True)),
                ('confirm_da', models.CharField(blank=True, max_length=36, null=True)),
                ('status', models.CharField(blank=True, max_length=30, null=True)),
                ('complete', models.CharField(blank=True, max_length=30, null=True)),
                ('std_status', models.CharField(blank=True, max_length=90, null=True)),
                ('imp_all', models.CharField(blank=True, max_length=240, null=True)),
                ('syll', models.CharField(blank=True, max_length=90, null=True)),
                ('syll_yr', models.CharField(blank=True, max_length=90, null=True)),
                ('confirm_d1', models.CharField(blank=True, max_length=90, null=True)),
                ('sif_sub', models.CharField(blank=True, max_length=120, null=True)),
                ('pic_sessio', models.CharField(blank=True, max_length=12, null=True)),
                ('session_ty', models.CharField(blank=True, max_length=20, null=True)),
                ('admission_field', models.CharField(blank=True, db_column='admission_', max_length=10, null=True)),
                ('id', models.BigAutoField(db_column='ID', primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'degsif18y3010919',
                'managed': False,
            },
        ),
    ]
