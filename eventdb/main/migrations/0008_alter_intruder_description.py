# Generated by Django 4.2 on 2023-04-24 14:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_alter_intruder_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='intruder',
            name='description',
            field=models.TextField(default='Нет описания (Нежелательное поведение)', verbose_name='Описание нарушителя'),
        ),
    ]
