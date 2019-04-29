# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('perfis', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Convite',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('convidado', models.ForeignKey(related_name='convites_recebidos', to='perfis.Perfil')),
                ('solicitante', models.ForeignKey(related_name='convites_feitos', to='perfis.Perfil')),
            ],
        ),
    ]
