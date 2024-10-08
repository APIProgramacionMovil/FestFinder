# Generated by Django 5.1.1 on 2024-09-15 00:09

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0012_valoracionestablecimiento'),
    ]

    operations = [
        migrations.CreateModel(
            name='Asistencia',
            fields=[
                ('id_asistencia', models.AutoField(primary_key=True, serialize=False)),
                ('id_evento_asistido_fk', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.establecimiento')),
                ('id_usuario_fk', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.usuario')),
            ],
        ),
    ]
