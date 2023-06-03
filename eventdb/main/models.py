from django.db import models
# from django.forms import ModelForm
from django import utils
from datetime import datetime

from django.shortcuts import get_object_or_404

from django.contrib.auth.models import User


def get_upload_path(instance, filename):
    return "persons_files/images/{0}/{1}".format(instance.fio, filename)

def get_upload_path_file(instance, filename):
    person = get_object_or_404(Person, id=instance.person_id)
    return "persons_files/files/{0}/{1}".format(person.fio, filename)

def get_upload_path_file_event(instance, filename):
    event = get_object_or_404(Event, id=instance.event_id)
    return "event_files/files/{0}/{1}".format(event.id, filename)


class Event(models.Model):
    id = models.AutoField(primary_key=True, verbose_name='№ п.п.')
    type = models.CharField(max_length=100, verbose_name='Вид события')
    date_incedent = models.DateTimeField(verbose_name='Дата проишествия')

    author = models.CharField(max_length=100, verbose_name='Автор')
    change_date = models.DateTimeField(auto_now=True, verbose_name='Дата изменения')

    entity = models.CharField(verbose_name='Юридическое лицо', blank=True, null=True, default='-')
    division = models.CharField(max_length=100, verbose_name='Дивизион', blank=True, null=True, default='-')
    filial = models.CharField(max_length=200, verbose_name='Филиал', blank=True, null=True, default='-')
    representation = models.CharField(verbose_name='Представительство', blank=True, null=True, default='-')

    description = models.TextField(verbose_name='Описание события')
    way = models.CharField(verbose_name='Способ проникновения', max_length=40)
    instrument = models.CharField(verbose_name='Средство совершения', max_length=100)
    relation = models.CharField(max_length=100, verbose_name='В отношении')
    object = models.CharField(max_length=150, verbose_name='Предмет посягательства')
    place = models.CharField(max_length=300, verbose_name='Место')

    class Meta:
        verbose_name = 'Событие'
        verbose_name_plural = 'СОБЫТИЯ: События'
        
    def __iter__(self):
        for field in self._meta.fields:
            if field.verbose_name == 'Дата проишествия':
                yield (field.verbose_name, datetime.strftime(datetime.strptime(field.value_to_string(self), '%Y-%m-%dT%H:%M:%S'), '%d.%m.%Y %H:%M'))
            elif field.verbose_name == 'Дата изменения':
                yield (field.verbose_name, datetime.strftime(datetime.strptime(field.value_to_string(self), '%Y-%m-%dT%H:%M:%S.%f'), '%d.%m.%Y %H:%M'))
            else:
                yield (field.verbose_name,  field.value_to_string(self))

    def __str__(self):
	    return 'ID события: ' + str(self.id) + ' | Дата: ' + str(self.date_incedent)
    

    
class RelatedPerson(models.Model):
    id_event = models.IntegerField(verbose_name='Номер события')
    role = models.CharField(verbose_name='Роль:')
    role_desc = models.CharField(verbose_name='Кем является:', blank=True, null=True, default=None)
    id_person = models.IntegerField(verbose_name='ID лица')

    class Meta:
        verbose_name = 'Связанное лицо'
        verbose_name_plural = 'ЛИЦА: Связанные лица'

    def __iter__(self):
        for field in self._meta.fields:
             yield (field.verbose_name,  field.value_to_string(self))

    def __str__(self):
        return 'ID события: ' + str(self.id_event) + ' | Роль: ' + self.role


class Person(models.Model):
    def __init__(self, *args, **kwargs):
        super(Person, self).__init__(*args, **kwargs)
        self.fio = self.last_name + ' ' + self.first_name + ' ' + self.second_name
    id = models.AutoField(primary_key=True, verbose_name='ID лица')
    add_at = models.DateTimeField(default=utils.timezone.now, editable=False)

    fio = models.CharField(max_length=100, verbose_name='ФИО')
    last_name = models.CharField(max_length=30, verbose_name='Фамилия', blank=True)
    first_name = models.CharField(max_length=30, verbose_name='Имя', blank=True)
    second_name = models.CharField(max_length=30, verbose_name='Отчество', blank=True)
    description = models.TextField(verbose_name='Описание лица', default='Нет описания (Нежелательное поведение)')
    sex = models.CharField(verbose_name='Пол', choices=(('м', 'М'), ('ж', 'Ж')))
    birthday = models.DateField(verbose_name='Дата рождения', null=True, blank=True)

    id_related = models.IntegerField(verbose_name='FK related', default=None, null=True)

    author = models.CharField(verbose_name='Автор', default=None)  

    person_image = models.ImageField(verbose_name='Фото лица', upload_to=get_upload_path, blank=True, null=True, default=None)
    # file = models.File

    class Meta:
        verbose_name = 'Лицо'
        verbose_name_plural = 'ЛИЦА: Лица'
        
    def __iter__(self):
        for field in self._meta.fields:
            yield (field.verbose_name,  field.value_to_string(self))

    def __str__(self):
  	    return self.fio + ' | ' + str(self.birthday)



class AdressesPlacesOfBirth(models.Model):
    id_place_of_birth = models.ForeignKey(Person, on_delete=models.CASCADE, to_field='id')
    country = models.CharField(verbose_name='Страна', blank=True)
    region = models.CharField(verbose_name='Область', blank=True)
    adress = models.TextField(verbose_name='Адрес', blank=True)
    who_added = models.CharField(verbose_name='Добавил:', blank=False, default='-')

    class Meta:
        verbose_name = 'Место рождения'
        verbose_name_plural = 'АДРЕСА: Места рождения'
        
    def __iter__(self):
        for field in self._meta.fields:
             yield (field.verbose_name,  field.value_to_string(self))

    def __str__(self):
	    return 'ID места рождения: ' + str(self.id)

class AdressesPlacesOfWork(models.Model):
    id_place_of_work = models.ForeignKey(Person, on_delete=models.CASCADE, to_field='id')

    entity = models.CharField(verbose_name='Юридическое лицо', blank=False, default='-')
    division = models.CharField(max_length=100, verbose_name='Дивизион')
    filial = models.CharField(max_length=200, verbose_name='Филиал')
    representation = models.CharField(verbose_name='Представительство')

    who_added = models.CharField(verbose_name='Добавил:', blank=False, default='-')

    class Meta:
        verbose_name = 'Место работы'
        verbose_name_plural = 'АДРЕСА: Места работы'
        
    def __iter__(self):
        for field in self._meta.fields:
            yield (field.verbose_name,  field.value_to_string(self))

    def __str__(self):
	    return 'ID места работы: ' + str(self.id)

class AdressesPlacesOfLive(models.Model):
    id_place_of_live = models.ForeignKey(Person, on_delete=models.CASCADE, to_field='id')
    country = models.CharField(verbose_name='Страна', blank=True)
    region = models.CharField(verbose_name='Область', blank=True)
    area = models.CharField(verbose_name='Район', blank=True)
    locality = models.CharField(verbose_name='Населенный пункт', blank=True)
    street = models.CharField(verbose_name='Улица', blank=True)
    house = models.CharField(verbose_name='Дом', blank=True)
    frame = models.CharField(verbose_name='Корпус', blank=True)
    apartment = models.CharField(verbose_name='Квартира', blank=True)
    who_added = models.CharField(verbose_name='Добавил:', blank=False, default='-')

    class Meta:
        verbose_name = 'Место регистрации'
        verbose_name_plural = 'АДРЕСА: Места регистрации'
        
    def __iter__(self):
        for field in self._meta.fields:
             yield (field.verbose_name,  field.value_to_string(self))

    def __str__(self):
	    return 'ID места регистрации: ' + str(self.id)

class OtherAdresses(models.Model):
    id_other_places = models.ForeignKey(Person, on_delete=models.CASCADE, to_field='id')
    description = models.CharField(verbose_name='Описание адреса', blank=True)
    country = models.CharField(verbose_name='Страна', blank=True)
    region = models.CharField(verbose_name='Область', blank=True)
    area = models.CharField(verbose_name='Район', blank=True)
    locality = models.CharField(verbose_name='Населенный пункт', blank=True)
    street = models.CharField(verbose_name='Улица', blank=True)
    house = models.CharField(verbose_name='Дом', blank=True)
    frame = models.CharField(verbose_name='Корпус', blank=True)
    apartment = models.CharField(verbose_name='Квартира', blank=True)
    who_added = models.CharField(verbose_name='Добавил:', blank=False, default='-')

    class Meta:
        verbose_name = 'Остальной адрес'
        verbose_name_plural = 'АДРЕСА: Остальные адреса'
        
    def __iter__(self):
        for field in self._meta.fields:
             yield (field.verbose_name,  field.value_to_string(self))

    def __str__(self):
	    return 'ID адреса: ' + str(self.id)
    

class Changes(models.Model):
    id_user = models.IntegerField(verbose_name='Автор:')
    
    record_name = models.CharField(verbose_name='Тип записи:')
    id_record = models.IntegerField(verbose_name='ID записи:')
    time_change = models.DateTimeField(verbose_name='Изменено в:', auto_now=utils.timezone.now)
    edit_from = models.CharField(verbose_name='Изменено с:', blank=True)
    edit_to = models.CharField(verbose_name='Изменено на:', blank=True)
    type_edit = models.CharField(verbose_name='Поле изменения:')

    class Meta:
        verbose_name = 'Изменение лица'
        verbose_name_plural = 'ЛИЦА: Изменения лиц'
        
    def __iter__(self):
        for field in self._meta.fields:
            if field.verbose_name == 'Изменено в:':
                yield (field.verbose_name, datetime.strftime(datetime.strptime(field.value_to_string(self), '%Y-%m-%dT%H:%M:%S.%f'), '%d.%m.%Y %H:%M'))
            elif field.verbose_name  == 'Автор:':
                user = User.objects.get(id=field.value_to_string(self))
                yield (field.verbose_name,  user.first_name + ' ' + user.last_name)
            elif field.verbose_name not in ('ID лица:', 'ID'):
                yield (field.verbose_name,  field.value_to_string(self))
            

    def __str__(self):
	    return 'ID изменения: ' + str(self.id)
    

class ChangesEvent(models.Model):
    id_user = models.IntegerField(verbose_name='Автор:')
    id_record = models.IntegerField(verbose_name='ID записи:')
    record_name = models.CharField(verbose_name='Тип записи:')

    time_change = models.DateTimeField(verbose_name='Изменено в:', auto_now_add=utils.timezone.now)
    edit_from = models.TextField(verbose_name='Изменено с:', blank=True)
    edit_to = models.TextField(verbose_name='Изменено на:', blank=True)

    class Meta:
        verbose_name = 'Изменение события'
        verbose_name_plural = 'СОБЫТИЯ: Изменения событий'
        
    def __iter__(self):
        for field in self._meta.fields:
             yield (field.verbose_name,  field.value_to_string(self))

    def __str__(self):
        author = User.objects.get(id=self.id_user)
        return 'Автор: ' + author.last_name + ' ' + author.first_name +  ' | ID события: ' + str(self.id_record) + ' | ID изменения: ' + str(self.id)
    


class FilesPerson(models.Model):
    person_id = models.IntegerField(verbose_name='ID лица')
    file = models.FileField(verbose_name='Файл', upload_to=get_upload_path_file)
    filename = models.CharField(verbose_name='Название файла', default=None, blank=True, null=True)

    class Meta:
        verbose_name = 'Файл лица'
        verbose_name_plural = 'ЛИЦА: Файлы лиц'
        
    def __iter__(self):
        for field in self._meta.fields:
             yield (field.verbose_name,  field.value_to_string(self))

    def __str__(self):
        person = Person.objects.get(id=self.person_id)
        return 'Лицо: ' + str(person.fio) + '| Файл: ' + str(self.filename)
    


class FilesEvent(models.Model):
    event_id = models.IntegerField(verbose_name='ID события')
    file = models.FileField(verbose_name='Файл', upload_to=get_upload_path_file_event)
    filename = models.CharField(verbose_name='Название файла', default=None, blank=True, null=True)

    class Meta:
        verbose_name = 'Файл события'
        verbose_name_plural = 'СОБЫТИЯ: Файлы событий'
        
    def __iter__(self):
        for field in self._meta.fields:
             yield (field.verbose_name,  field.value_to_string(self))

    def __str__(self):
        return 'Событие: ' + str(self.event_id) + '| Файл: ' + str(self.filename)
    

class Entity(models.Model):
    id_entity = models.AutoField(primary_key=True, verbose_name='ID юридического лица')
    name = models.CharField(verbose_name='Юридическое лицо')

    class Meta:
        verbose_name = 'Юридическое лицо'
        verbose_name_plural = 'БИБИЛИОТЕКА: Юридические лица'

    def __str__(self):
        return 'ID: ' + str(self.id_entity) + ' | ' + self.name

class Division(models.Model):
    id_entity = models.ForeignKey(Entity, on_delete=models.CASCADE, to_field='id_entity')
    id_division = models.AutoField(verbose_name='ID дивизиона', primary_key=True)
    name = models.CharField(verbose_name='Дивизион')

    class Meta:
        verbose_name = 'Дивизион'
        verbose_name_plural = 'БИБИЛИОТЕКА: Дивизионы'

    def __str__(self):
        return 'ID: ' + str(self.id_division) + ' | ' + self.name

class Filial(models.Model):
    id_division = models.ForeignKey(Division, on_delete=models.CASCADE, to_field='id_division')
    id_filial = models.AutoField(verbose_name='ID филиала', primary_key=True)
    name = models.CharField(verbose_name='Филиал')

    class Meta:
        verbose_name = 'Филиал'
        verbose_name_plural = 'БИБИЛИОТЕКА: Филиалы'

    def __str__(self):
        return 'ID: ' + str(self.id_filial) + ' | ' + self.name
    
class Representation(models.Model):
    id_filial = models.ForeignKey(Filial, on_delete=models.CASCADE, to_field='id_filial')
    id_rep = models.AutoField(verbose_name='ID представительства', primary_key=True)
    name = models.CharField(verbose_name='Филиал')

    class Meta:
        verbose_name = 'Представительство'
        verbose_name_plural = 'БИБИЛИОТЕКА: Представительства'

    def __str__(self):
        return 'ID: ' + str(self.id_rep) + ' | ' + self.name

class Logging(models.Model):
    author = models.CharField(verbose_name='Автор')
    type = models.CharField(verbose_name='Тип', default='')
    logged_event = models.TextField(verbose_name='Что сделал')
    datetime = models.DateTimeField(auto_now=utils.timezone.now, verbose_name='Время')

    class Meta:
        verbose_name = 'Лог'
        verbose_name_plural = 'ЛОГГИРОВАНИЕ: Логи'


class LoggingUser(models.Model):
    author = models.CharField(verbose_name='Автор')
    type = models.CharField(verbose_name='Что сделал')
    datetime = models.DateTimeField(auto_now=utils.timezone.now, verbose_name='Время')

    class Meta:
        verbose_name = 'Лог входа/выхода'
        verbose_name_plural = 'ЛОГГИРОВАНИЕ: Логи входа/выхода'
