# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0003_company_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='slug',
            field=models.SlugField(unique=True, blank=True),
        ),
    ]
