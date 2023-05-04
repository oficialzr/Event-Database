# Generated by Django 4.2 on 2023-05-03 13:39

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_divisions_filials_alter_person_add_at_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='who_added',
            field=models.CharField(default='-', verbose_name='Добавил:'),
        ),
        migrations.AlterField(
            model_name='person',
            name='add_at',
            field=models.DateTimeField(default=datetime.datetime(2023, 5, 3, 13, 39, 37, 604109), editable=False),
        ),
    ]