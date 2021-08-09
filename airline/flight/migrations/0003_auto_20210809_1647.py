# Generated by Django 3.2.5 on 2021-08-09 09:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flight', '0002_passenger'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='passenger',
            name='flight',
        ),
        migrations.AddField(
            model_name='passenger',
            name='flight',
            field=models.ManyToManyField(blank=True, related_name='passengers', to='flight.Flight'),
        ),
    ]
