# Generated by Django 5.1.6 on 2025-03-12 04:39

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_plate_highest_bid_alter_bid_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bid',
            name='plate',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bids', related_query_name='bids', to='app.plate'),
        ),
    ]
