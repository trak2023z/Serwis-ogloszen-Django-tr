# Generated by Django 3.2.18 on 2023-05-04 14:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('SerwisOgloszenApp', '0005_auto_20230422_2002'),
    ]

    operations = [
        migrations.AddField(
            model_name='ad',
            name='reserver',
            field=models.OneToOneField(blank=True, default='', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='reserver', to='SerwisOgloszenApp.customer'),
        ),
    ]
