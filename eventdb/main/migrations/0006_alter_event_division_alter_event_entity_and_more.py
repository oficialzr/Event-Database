# Generated by Django 4.2 on 2023-05-26 15:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_alter_event_division_alter_event_entity_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='division',
            field=models.CharField(blank=True, default='-', max_length=100, null=True, verbose_name='Дивизион'),
        ),
        migrations.AlterField(
            model_name='event',
            name='entity',
            field=models.CharField(blank=True, default='-', null=True, verbose_name='Юридическое лицо'),
        ),
        migrations.AlterField(
            model_name='event',
            name='filial',
            field=models.CharField(blank=True, default='-', max_length=200, null=True, verbose_name='Филиал'),
        ),
        migrations.AlterField(
            model_name='event',
            name='representation',
            field=models.CharField(blank=True, default='-', null=True, verbose_name='Представительство'),
        ),
    ]
