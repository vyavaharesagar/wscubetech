# Generated by Django 4.0.4 on 2023-06-07 05:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('leads', '0007_leadhistory_diposition'),
    ]

    operations = [
        migrations.RenameField(
            model_name='leadhistory',
            old_name='diposition',
            new_name='disposition',
        ),
    ]
