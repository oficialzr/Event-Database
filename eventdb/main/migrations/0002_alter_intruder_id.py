# Generated by Django 4.2 on 2023-04-23 19:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='intruder',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
