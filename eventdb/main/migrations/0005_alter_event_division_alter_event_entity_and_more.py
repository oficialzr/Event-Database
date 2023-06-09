# Generated by Django 4.2 on 2023-05-26 14:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_alter_representation_id_filial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='division',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Дивизион'),
        ),
        migrations.AlterField(
            model_name='event',
            name='entity',
            field=models.CharField(blank=True, null=True, verbose_name='Юридическое лицо'),
        ),
        migrations.AlterField(
            model_name='event',
            name='filial',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Филиал'),
        ),
        migrations.AlterField(
            model_name='event',
            name='representation',
            field=models.CharField(blank=True, null=True, verbose_name='Представительство'),
        ),
    ]
