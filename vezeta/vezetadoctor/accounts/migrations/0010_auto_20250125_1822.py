# Generated by Django 3.1 on 2025-01-25 16:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0009_auto_20250125_1801'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='services',
        ),
        migrations.AddField(
            model_name='profile',
            name='services',
            field=models.TextField(blank=True, max_length=500, null=True),
        ),
        migrations.DeleteModel(
            name='Service',
        ),
    ]
