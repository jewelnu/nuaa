# Generated by Django 5.0.4 on 2024-08-23 13:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0002_alter_student_picture'),
    ]

    operations = [
        migrations.CreateModel(
            name='District',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('district', models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                'db_table': 'district',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Upozilla',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('district', models.CharField(blank=True, max_length=255, null=True)),
                ('upozilla', models.CharField(blank=True, max_length=255, null=True)),
                ('dist_id', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'upozilla',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AddressJob',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('present_address', models.TextField()),
                ('present_dist', models.TextField()),
                ('present_upozilla', models.TextField()),
                ('permanent_address', models.TextField()),
                ('permanent_dist', models.TextField()),
                ('permanent_upozilla', models.TextField()),
                ('work_address', models.TextField()),
                ('work_dist', models.TextField()),
                ('work_upozilla', models.TextField()),
            ],
        ),
    ]
