# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('HR', '0004_employee_company'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employee',
            name='company',
        ),
    ]
