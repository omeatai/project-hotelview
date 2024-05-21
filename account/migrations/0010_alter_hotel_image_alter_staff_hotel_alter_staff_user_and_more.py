# Generated by Django 5.0.4 on 2024-05-05 06:17

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0009_hotel_alter_user_options_user_phone_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hotel',
            name='image',
            field=models.FileField(upload_to='hotels'),
        ),
        migrations.AlterField(
            model_name='staff',
            name='hotel',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='staff_hotel', to='account.hotel'),
        ),
        migrations.AlterField(
            model_name='staff',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='staff_user', to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='Owner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hotel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='owner_hotel', to='account.hotel')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='owner_user', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Owner',
                'verbose_name_plural': 'Owners',
                'ordering': ['user'],
            },
        ),
    ]