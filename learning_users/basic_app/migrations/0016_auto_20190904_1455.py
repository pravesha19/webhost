# Generated by Django 2.1.7 on 2019-09-04 14:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('basic_app', '0015_auto_20190904_1453'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofileinfo',
            name='college',
            field=models.CharField(default=None, max_length=120),
        ),
        migrations.AlterField(
            model_name='userprofileinfo',
            name='college_reg_id',
            field=models.CharField(default=None, max_length=50),
        ),
        migrations.AlterField(
            model_name='userprofileinfo',
            name='dept',
            field=models.CharField(default=None, max_length=120),
        ),
        migrations.AlterField(
            model_name='userprofileinfo',
            name='mob_no',
            field=models.CharField(default=None, max_length=10),
        ),
    ]