# Generated by Django 3.0.8 on 2020-07-28 06:00

import django.contrib.gis.db.models.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0008_auto_20200728_0549'),
    ]

    operations = [
        migrations.AlterField(
            model_name='roi',
            name='geom',
            field=django.contrib.gis.db.models.fields.GeometryCollectionField(srid=4326),
        ),
        migrations.AlterField(
            model_name='roi_divided',
            name='geom',
            field=django.contrib.gis.db.models.fields.GeometryCollectionField(srid=4326),
        ),
    ]
