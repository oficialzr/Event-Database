# Generated by Django 4.2 on 2023-04-30 13:20

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_alter_relatedperson_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='add_at',
            field=models.DateTimeField(default=datetime.datetime(2023, 4, 30, 13, 20, 8, 221355)),
        ),
    ]
