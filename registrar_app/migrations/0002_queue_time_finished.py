# Generated by Django 4.2 on 2023-06-20 08:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registrar_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='queue',
            name='time_finished',
            field=models.TimeField(blank=True, null=True),
        ),
    ]
