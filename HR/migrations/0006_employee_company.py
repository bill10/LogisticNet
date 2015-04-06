# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0004_auto_20150405_0536'),
        ('HR', '0005_remove_employee_company'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='company',
            field=models.ForeignKey(default='', to='company.Company'),
            preserve_default=False,
        ),
    ]
