# Generated by Django 4.2 on 2023-05-19 14:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_alter_event_change_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='change_date',
            field=models.DateTimeField(auto_now=True, verbose_name='Дата изменения'),
        ),
    ]