# Generated by Django 5.1.3 on 2024-11-13 04:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='RespuestaFormulario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('correo', models.EmailField(max_length=254)),
                ('duda', models.TextField()),
                ('fecha', models.DateField()),
                ('informacion', models.CharField(choices=[('Sí', 'Sí'), ('No', 'No')], max_length=10)),
            ],
        ),
    ]
