# Generated by Django 3.1.6 on 2021-02-21 08:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('PPDS', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='attackerdata',
            old_name='patient_id',
            new_name='patient',
        ),
    ]
