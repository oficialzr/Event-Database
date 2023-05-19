# Generated by Django 4.2 on 2023-05-19 14:07

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import main.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Changes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_user', models.IntegerField(verbose_name='Автор:')),
                ('record_name', models.CharField(verbose_name='Тип записи:')),
                ('id_record', models.IntegerField(verbose_name='ID записи:')),
                ('time_change', models.DateTimeField(auto_now_add=True, verbose_name='Изменено в:')),
                ('edit_from', models.CharField(blank=True, verbose_name='Изменено с:')),
                ('edit_to', models.CharField(blank=True, verbose_name='Изменено на:')),
                ('type_edit', models.CharField(verbose_name='Поле изменения:')),
            ],
            options={
                'verbose_name': 'Изменение лица',
                'verbose_name_plural': 'ЛИЦА: Изменения лиц',
            },
        ),
        migrations.CreateModel(
            name='ChangesEvent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_user', models.IntegerField(verbose_name='Автор:')),
                ('id_record', models.IntegerField(verbose_name='ID записи:')),
                ('record_name', models.CharField(verbose_name='Тип записи:')),
                ('time_change', models.DateTimeField(auto_now_add=True, verbose_name='Изменено в:')),
                ('edit_from', models.TextField(blank=True, verbose_name='Изменено с:')),
                ('edit_to', models.TextField(blank=True, verbose_name='Изменено на:')),
            ],
            options={
                'verbose_name': 'Изменение события',
                'verbose_name_plural': 'СОБЫТИЯ: Изменения событий',
            },
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='№ п.п.')),
                ('date_incedent', models.DateTimeField(verbose_name='Дата проишествия')),
                ('author', models.CharField(max_length=100, verbose_name='ФИО автора')),
                ('change_date', models.DateField(auto_now_add=True, verbose_name='Дата изменения')),
                ('division', models.CharField(max_length=100, verbose_name='Дивизион')),
                ('filial', models.CharField(max_length=200, verbose_name='Филиал')),
                ('representation', models.CharField(verbose_name='Представительство')),
                ('entity', models.CharField(verbose_name='Юридическое лицо')),
                ('description', models.TextField(verbose_name='Описание события')),
                ('type', models.CharField(max_length=100, verbose_name='Вид события')),
                ('way', models.CharField(max_length=40, verbose_name='Способ проникновения')),
                ('instrument', models.CharField(max_length=100, verbose_name='Средство совершения')),
                ('relation', models.CharField(max_length=100, verbose_name='В отношении')),
                ('object', models.CharField(max_length=150, verbose_name='Предмет посягательства')),
                ('place', models.CharField(max_length=300, verbose_name='Место')),
            ],
            options={
                'verbose_name': 'Событие',
                'verbose_name_plural': 'СОБЫТИЯ: События',
            },
        ),
        migrations.CreateModel(
            name='FilesEvent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event_id', models.IntegerField(verbose_name='ID события')),
                ('file', models.FileField(upload_to=main.models.get_upload_path_file_event, verbose_name='Файл')),
                ('filename', models.CharField(blank=True, default=None, null=True, verbose_name='Название файла')),
            ],
            options={
                'verbose_name': 'Файл события',
                'verbose_name_plural': 'СОБЫТИЯ: Файлы событий',
            },
        ),
        migrations.CreateModel(
            name='FilesPerson',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('person_id', models.IntegerField(verbose_name='ID лица')),
                ('file', models.FileField(upload_to=main.models.get_upload_path_file, verbose_name='Файл')),
                ('filename', models.CharField(blank=True, default=None, null=True, verbose_name='Название файла')),
            ],
            options={
                'verbose_name': 'Файл лица',
                'verbose_name_plural': 'ЛИЦА: Файлы лиц',
            },
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID лица')),
                ('add_at', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
                ('fio', models.CharField(max_length=100, verbose_name='ФИО')),
                ('last_name', models.CharField(blank=True, max_length=30, verbose_name='Фамилия')),
                ('first_name', models.CharField(blank=True, max_length=30, verbose_name='Имя')),
                ('second_name', models.CharField(blank=True, max_length=30, verbose_name='Отчество')),
                ('description', models.TextField(default='Нет описания (Нежелательное поведение)', verbose_name='Описание лица')),
                ('sex', models.CharField(choices=[('м', 'М'), ('ж', 'Ж')], verbose_name='Пол')),
                ('birthday', models.DateField(blank=True, null=True, verbose_name='Дата рождения')),
                ('id_related', models.IntegerField(default=None, null=True, verbose_name='FK related')),
                ('author', models.CharField(default=None, verbose_name='Автор')),
                ('person_image', models.ImageField(blank=True, default=None, null=True, upload_to=main.models.get_upload_path, verbose_name='Фото лица')),
            ],
            options={
                'verbose_name': 'Лицо',
                'verbose_name_plural': 'ЛИЦА: Лица',
            },
        ),
        migrations.CreateModel(
            name='RelatedPerson',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_event', models.IntegerField(verbose_name='Номер события')),
                ('role', models.CharField(verbose_name='Роль:')),
                ('role_desc', models.CharField(blank=True, default=None, null=True, verbose_name='Кем является:')),
                ('id_person', models.IntegerField(verbose_name='ID лица')),
            ],
            options={
                'verbose_name': 'Связанное лицо',
                'verbose_name_plural': 'ЛИЦА: Связанные лица',
            },
        ),
        migrations.CreateModel(
            name='OtherAdresses',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(blank=True, verbose_name='Описание адреса')),
                ('country', models.CharField(blank=True, verbose_name='Страна')),
                ('region', models.CharField(blank=True, verbose_name='Область')),
                ('area', models.CharField(blank=True, verbose_name='Район')),
                ('locality', models.CharField(blank=True, verbose_name='Населенный пункт')),
                ('street', models.CharField(blank=True, verbose_name='Улица')),
                ('house', models.CharField(blank=True, verbose_name='Дом')),
                ('frame', models.CharField(blank=True, verbose_name='Корпус')),
                ('apartment', models.CharField(blank=True, verbose_name='Квартира')),
                ('who_added', models.CharField(default='-', verbose_name='Добавил:')),
                ('id_other_places', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.person')),
            ],
            options={
                'verbose_name': 'Остальной адрес',
                'verbose_name_plural': 'АДРЕСА: Остальные адреса',
            },
        ),
        migrations.CreateModel(
            name='AdressesPlacesOfWork',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('entity', models.CharField(default='-', verbose_name='Юридическое лицо')),
                ('country', models.CharField(blank=True, verbose_name='Страна')),
                ('region', models.CharField(blank=True, verbose_name='Область')),
                ('area', models.CharField(blank=True, verbose_name='Район')),
                ('locality', models.CharField(blank=True, verbose_name='Населенный пункт')),
                ('street', models.CharField(blank=True, verbose_name='Улица')),
                ('house', models.CharField(blank=True, verbose_name='Дом')),
                ('frame', models.CharField(blank=True, verbose_name='Корпус')),
                ('apartment', models.CharField(blank=True, verbose_name='Квартира')),
                ('who_added', models.CharField(default='-', verbose_name='Добавил:')),
                ('id_place_of_work', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.person')),
            ],
            options={
                'verbose_name': 'Место работы',
                'verbose_name_plural': 'АДРЕСА: Места работы',
            },
        ),
        migrations.CreateModel(
            name='AdressesPlacesOfLive',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country', models.CharField(blank=True, verbose_name='Страна')),
                ('region', models.CharField(blank=True, verbose_name='Область')),
                ('area', models.CharField(blank=True, verbose_name='Район')),
                ('locality', models.CharField(blank=True, verbose_name='Населенный пункт')),
                ('street', models.CharField(blank=True, verbose_name='Улица')),
                ('house', models.CharField(blank=True, verbose_name='Дом')),
                ('frame', models.CharField(blank=True, verbose_name='Корпус')),
                ('apartment', models.CharField(blank=True, verbose_name='Квартира')),
                ('who_added', models.CharField(default='-', verbose_name='Добавил:')),
                ('id_place_of_live', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.person')),
            ],
            options={
                'verbose_name': 'Место регистрации',
                'verbose_name_plural': 'АДРЕСА: Места регистрации',
            },
        ),
        migrations.CreateModel(
            name='AdressesPlacesOfBirth',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country', models.CharField(blank=True, verbose_name='Страна')),
                ('region', models.CharField(blank=True, verbose_name='Область')),
                ('adress', models.TextField(blank=True, verbose_name='Адрес')),
                ('who_added', models.CharField(default='-', verbose_name='Добавил:')),
                ('id_place_of_birth', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.person')),
            ],
            options={
                'verbose_name': 'Место рождения',
                'verbose_name_plural': 'АДРЕСА: Места рождения',
            },
        ),
    ]
