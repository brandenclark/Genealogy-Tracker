# Generated by Django 2.0.3 on 2018-04-07 14:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0002_person_raffle'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='raffle',
            field=models.TextField(default='A'),
        ),
    ]
