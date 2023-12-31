# Generated by Django 3.2.9 on 2023-04-25 21:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data1', '0007_rename_actualizacion_actualizacion1'),
    ]

    operations = [
        migrations.CreateModel(
            name='Actualizacion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('valor1', models.CharField(max_length=100, verbose_name='$CBT')),
                ('valor2', models.CharField(max_length=100, verbose_name='$m2')),
                ('valor3', models.CharField(max_length=100, verbose_name='$Auto')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='fecha de creación')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='fecha de modificación')),
            ],
            options={
                'verbose_name': 'actualización',
                'verbose_name_plural': 'actualizaciones',
                'ordering': ['-created'],
            },
        ),
        migrations.DeleteModel(
            name='Actualizacion1',
        ),
    ]
