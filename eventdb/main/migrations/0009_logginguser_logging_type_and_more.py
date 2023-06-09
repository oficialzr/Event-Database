# Generated by Django 4.2 on 2023-05-31 15:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_alter_adressesplacesofbirth_country_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='LoggingUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.CharField(verbose_name='Автор')),
                ('type', models.CharField(verbose_name='Что сделал')),
                ('datetime', models.DateTimeField(auto_now=True, verbose_name='Время')),
            ],
        ),
        migrations.AddField(
            model_name='logging',
            name='type',
            field=models.CharField(default='', verbose_name='Тип'),
        ),
        migrations.AlterField(
            model_name='adressesplacesofbirth',
            name='country',
            field=models.CharField(blank=True, verbose_name='Страна'),
        ),
        migrations.AlterField(
            model_name='adressesplacesofbirth',
            name='region',
            field=models.CharField(blank=True, verbose_name='Область'),
        ),
        migrations.AlterField(
            model_name='adressesplacesofbirth',
            name='who_added',
            field=models.CharField(default='-', verbose_name='Добавил:'),
        ),
        migrations.AlterField(
            model_name='adressesplacesoflive',
            name='apartment',
            field=models.CharField(blank=True, verbose_name='Квартира'),
        ),
        migrations.AlterField(
            model_name='adressesplacesoflive',
            name='area',
            field=models.CharField(blank=True, verbose_name='Район'),
        ),
        migrations.AlterField(
            model_name='adressesplacesoflive',
            name='country',
            field=models.CharField(blank=True, verbose_name='Страна'),
        ),
        migrations.AlterField(
            model_name='adressesplacesoflive',
            name='frame',
            field=models.CharField(blank=True, verbose_name='Корпус'),
        ),
        migrations.AlterField(
            model_name='adressesplacesoflive',
            name='house',
            field=models.CharField(blank=True, verbose_name='Дом'),
        ),
        migrations.AlterField(
            model_name='adressesplacesoflive',
            name='locality',
            field=models.CharField(blank=True, verbose_name='Населенный пункт'),
        ),
        migrations.AlterField(
            model_name='adressesplacesoflive',
            name='region',
            field=models.CharField(blank=True, verbose_name='Область'),
        ),
        migrations.AlterField(
            model_name='adressesplacesoflive',
            name='street',
            field=models.CharField(blank=True, verbose_name='Улица'),
        ),
        migrations.AlterField(
            model_name='adressesplacesoflive',
            name='who_added',
            field=models.CharField(default='-', verbose_name='Добавил:'),
        ),
        migrations.AlterField(
            model_name='adressesplacesofwork',
            name='entity',
            field=models.CharField(default='-', verbose_name='Юридическое лицо'),
        ),
        migrations.AlterField(
            model_name='adressesplacesofwork',
            name='representation',
            field=models.CharField(verbose_name='Представительство'),
        ),
        migrations.AlterField(
            model_name='adressesplacesofwork',
            name='who_added',
            field=models.CharField(default='-', verbose_name='Добавил:'),
        ),
        migrations.AlterField(
            model_name='changes',
            name='edit_from',
            field=models.CharField(blank=True, verbose_name='Изменено с:'),
        ),
        migrations.AlterField(
            model_name='changes',
            name='edit_to',
            field=models.CharField(blank=True, verbose_name='Изменено на:'),
        ),
        migrations.AlterField(
            model_name='changes',
            name='record_name',
            field=models.CharField(verbose_name='Тип записи:'),
        ),
        migrations.AlterField(
            model_name='changes',
            name='type_edit',
            field=models.CharField(verbose_name='Поле изменения:'),
        ),
        migrations.AlterField(
            model_name='changesevent',
            name='record_name',
            field=models.CharField(verbose_name='Тип записи:'),
        ),
        migrations.AlterField(
            model_name='division',
            name='name',
            field=models.CharField(verbose_name='Дивизион'),
        ),
        migrations.AlterField(
            model_name='entity',
            name='name',
            field=models.CharField(verbose_name='Юридическое лицо'),
        ),
        migrations.AlterField(
            model_name='event',
            name='entity',
            field=models.CharField(blank=True, default='-', null=True, verbose_name='Юридическое лицо'),
        ),
        migrations.AlterField(
            model_name='event',
            name='representation',
            field=models.CharField(blank=True, default='-', null=True, verbose_name='Представительство'),
        ),
        migrations.AlterField(
            model_name='filesevent',
            name='filename',
            field=models.CharField(blank=True, default=None, null=True, verbose_name='Название файла'),
        ),
        migrations.AlterField(
            model_name='filesperson',
            name='filename',
            field=models.CharField(blank=True, default=None, null=True, verbose_name='Название файла'),
        ),
        migrations.AlterField(
            model_name='filial',
            name='name',
            field=models.CharField(verbose_name='Филиал'),
        ),
        migrations.AlterField(
            model_name='logging',
            name='author',
            field=models.CharField(verbose_name='Автор'),
        ),
        migrations.AlterField(
            model_name='otheradresses',
            name='apartment',
            field=models.CharField(blank=True, verbose_name='Квартира'),
        ),
        migrations.AlterField(
            model_name='otheradresses',
            name='area',
            field=models.CharField(blank=True, verbose_name='Район'),
        ),
        migrations.AlterField(
            model_name='otheradresses',
            name='country',
            field=models.CharField(blank=True, verbose_name='Страна'),
        ),
        migrations.AlterField(
            model_name='otheradresses',
            name='description',
            field=models.CharField(blank=True, verbose_name='Описание адреса'),
        ),
        migrations.AlterField(
            model_name='otheradresses',
            name='frame',
            field=models.CharField(blank=True, verbose_name='Корпус'),
        ),
        migrations.AlterField(
            model_name='otheradresses',
            name='house',
            field=models.CharField(blank=True, verbose_name='Дом'),
        ),
        migrations.AlterField(
            model_name='otheradresses',
            name='locality',
            field=models.CharField(blank=True, verbose_name='Населенный пункт'),
        ),
        migrations.AlterField(
            model_name='otheradresses',
            name='region',
            field=models.CharField(blank=True, verbose_name='Область'),
        ),
        migrations.AlterField(
            model_name='otheradresses',
            name='street',
            field=models.CharField(blank=True, verbose_name='Улица'),
        ),
        migrations.AlterField(
            model_name='otheradresses',
            name='who_added',
            field=models.CharField(default='-', verbose_name='Добавил:'),
        ),
        migrations.AlterField(
            model_name='person',
            name='author',
            field=models.CharField(default=None, verbose_name='Автор'),
        ),
        migrations.AlterField(
            model_name='person',
            name='sex',
            field=models.CharField(choices=[('м', 'М'), ('ж', 'Ж')], verbose_name='Пол'),
        ),
        migrations.AlterField(
            model_name='relatedperson',
            name='role',
            field=models.CharField(verbose_name='Роль:'),
        ),
        migrations.AlterField(
            model_name='relatedperson',
            name='role_desc',
            field=models.CharField(blank=True, default=None, null=True, verbose_name='Кем является:'),
        ),
        migrations.AlterField(
            model_name='representation',
            name='name',
            field=models.CharField(verbose_name='Филиал'),
        ),
    ]
