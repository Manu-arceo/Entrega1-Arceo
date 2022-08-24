# Generated by Django 4.0.6 on 2022-08-08 19:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CentroHistorico',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=120)),
                ('direccion', models.CharField(max_length=120)),
            ],
        ),
        migrations.CreateModel(
            name='Museos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=120)),
                ('direccion', models.CharField(max_length=120)),
                ('entrada', models.CharField(max_length=120)),
                ('contacto', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Parques',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=120)),
                ('direccion', models.CharField(max_length=120)),
            ],
        ),
    ]