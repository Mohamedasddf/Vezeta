# Generated by Django 5.1.5 on 2025-01-28 12:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0011_profile_user_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='name',
            field=models.CharField(blank=True, default='name', max_length=50),
        ),
        migrations.AlterField(
            model_name='profile',
            name='who_i',
            field=models.TextField(blank=True, default='who_i', max_length=500),
        ),
    ]
