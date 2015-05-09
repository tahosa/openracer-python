# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0002_auto_20150509_1007'),
    ]

    operations = [
        migrations.AddField(
            model_name='classes',
            name='abbr',
            field=models.CharField(max_length=4, null=True),
        ),
        migrations.AddField(
            model_name='drivers',
            name='scca_number',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='drivers',
            name='default_car',
            field=models.ForeignKey(to='events.Cars', null=True),
        ),
        migrations.AlterField(
            model_name='drivers',
            name='default_number',
            field=models.ForeignKey(to='events.Numbers', null=True),
        ),
        migrations.AlterUniqueTogether(
            name='eventdrivers',
            unique_together=set([('event', 'driver')]),
        ),
    ]
