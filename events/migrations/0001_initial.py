# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cars',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('make', models.CharField(max_length=50)),
                ('model', models.CharField(max_length=200)),
                ('year', models.CharField(max_length=4)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Classes',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=20)),
                ('parent', models.ForeignKey(to='events.Classes', null=True, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Drivers',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=200)),
                ('emergency_name', models.CharField(max_length=100)),
                ('emergency_phone', models.CharField(max_length=10)),
                ('novice', models.BooleanField(default=True)),
                ('default_car', models.ForeignKey(to='events.Cars')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='EventDrivers',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('car', models.ForeignKey(to='events.Cars')),
                ('driver', models.ForeignKey(to='events.Drivers')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Events',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('location', models.CharField(max_length=200)),
                ('name', models.CharField(max_length=200)),
                ('date', models.DateField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Numbers',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('number', models.IntegerField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Runs',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('time', models.DecimalField(decimal_places=3, max_digits=10)),
                ('cones', models.IntegerField()),
                ('gates', models.IntegerField()),
                ('driver', models.ForeignKey(to='events.EventDrivers')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='eventdrivers',
            name='event',
            field=models.ForeignKey(to='events.Events'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='eventdrivers',
            name='number',
            field=models.ForeignKey(to='events.Numbers'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='drivers',
            name='default_number',
            field=models.ForeignKey(to='events.Numbers'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='cars',
            name='car_class',
            field=models.ForeignKey(to='events.Classes'),
            preserve_default=True,
        ),
    ]
