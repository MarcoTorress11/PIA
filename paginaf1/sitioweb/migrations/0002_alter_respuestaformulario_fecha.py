# Generated by Django 5.1.3 on 2024-11-13 06:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sitioweb', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='respuestaformulario',
            name='fecha',
            field=models.DateTimeField(),
        ),
    ]
