# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('HR', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='job',
            field=models.ManyToManyField(help_text=b'Job', to='HR.Job'),
        ),
        migrations.AlterField(
            model_name='employee',
            name='name',
            field=models.CharField(help_text=b'Name', max_length=128),
        ),
    ]
