# Generated by Django 4.2 on 2023-04-23 23:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_alter_intruder_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='violations',
            name='change_date',
            field=models.DateField(auto_now_add=True, verbose_name='Дата изменения'),
        ),
        migrations.AlterField(
            model_name='violations',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False, verbose_name='№ п.п.'),
        ),
    ]
