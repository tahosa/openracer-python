# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='cars',
            name='driver_list',
            field=models.ManyToManyField(to='events.Drivers'),
        ),
        migrations.AddField(
            model_name='numbers',
            name='driver',
            field=models.ForeignKey(default=None, to='events.Drivers'),
            preserve_default=False,
        ),
    ]
