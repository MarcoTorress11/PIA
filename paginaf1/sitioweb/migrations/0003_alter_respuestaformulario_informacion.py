# Generated by Django 5.1.3 on 2024-11-14 00:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sitioweb', '0002_alter_respuestaformulario_fecha'),
    ]

    operations = [
        migrations.AlterField(
            model_name='respuestaformulario',
            name='informacion',
            field=models.CharField(choices=[('Si', 'Si'), ('No', 'No')], max_length=10),
        ),
    ]
