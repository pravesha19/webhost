# Generated by Django 2.1.7 on 2019-09-05 03:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('basic_app', '0020_log_refuser'),
    ]

    operations = [
        migrations.AlterField(
            model_name='log',
            name='refuser',
            field=models.CharField(default=None, max_length=10),
        ),
    ]
