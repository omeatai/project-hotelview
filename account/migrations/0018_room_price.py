# Generated by Django 5.0.4 on 2024-05-08 07:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0017_roomtype_room_sampleimage_room'),
    ]

    operations = [
        migrations.AddField(
            model_name='room',
            name='price',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
    ]
