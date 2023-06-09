# Generated by Django 4.2 on 2023-05-25 21:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_alter_division_options_alter_entity_options_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Representation',
            fields=[
                ('id_rep', models.AutoField(primary_key=True, serialize=False, verbose_name='ID представительства')),
                ('name', models.CharField(verbose_name='Филиал')),
                ('id_filial', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.division')),
            ],
            options={
                'verbose_name': 'Представительство',
                'verbose_name_plural': 'БИБИЛИОТЕКА: Представительства',
            },
        ),
    ]
