# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('perfis', '0002_convite'),
    ]

    operations = [
        migrations.AddField(
            model_name='perfil',
            name='amigos',
            field=models.ManyToManyField(related_name='amigos_rel_+', to='perfis.Perfil'),
        ),
    ]
