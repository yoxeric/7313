# Generated by Django 3.2.7 on 2024-10-28 16:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doublefactor', '0016_alter_otptoken_otp_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='otptoken',
            name='otp_code',
            field=models.CharField(default='1b7adb', max_length=6),
        ),
    ]
