from django.db import models


class Intruder(models.Model):
    id = models.AutoField(primary_key=True, verbose_name='ID нарушителя')
    intruder_fio = models.CharField(max_length=100, verbose_name='ФИО нарушителя')
    last_name = models.CharField(max_length=30, verbose_name='Фамилия', blank=True)
    first_name = models.CharField(max_length=30, verbose_name='Имя', blank=True)
    second_name = models.CharField(max_length=30, verbose_name='Отчество', blank=True)
    description = models.TextField(verbose_name='Описание нарушителя', default='Нет описания (Нежелательное поведение)')
    sex = models.CharField(max_length=1, verbose_name='Пол (м/ж)', blank=True)
    birthday = models.DateField(verbose_name='День рождения', null=True)
    with_companion = models.CharField(verbose_name='В компании с:', blank=True)
    adress_type = models.CharField(verbose_name='Тип адреса', blank=True)
    country = models.CharField(verbose_name='Страна', blank=True)
    region = models.CharField(verbose_name='Область', blank=True)
    area = models.CharField(verbose_name='Район', blank=True)
    locality = models.CharField(verbose_name='Населенный пункт', blank=True)
    street = models.CharField(verbose_name='Улица', blank=True)
    house = models.CharField(verbose_name='Дом', blank=True)
    frame = models.CharField(verbose_name='Корпус', blank=True)
    apartment = models.CharField(verbose_name='Квартира', blank=True)

    class Meta:
        verbose_name = 'Нарушитель'
        verbose_name_plural = 'Нарушители'

    def __iter__(self):
        for field in self._meta.fields:
             yield (field.verbose_name,  field.value_to_string(self))

    def __str__(self):
	    return self.intruder_fio
    #  + ' | ' + str(self.birthday)
    


class Violations(models.Model):
    id = models.AutoField(primary_key=True, verbose_name='№ п.п.')
    date_incedent = models.DateField(verbose_name='Дата проишествия')
    type = models.CharField(max_length=100, verbose_name='Тип проишествия')
    intruder = models.ForeignKey(Intruder, on_delete=models.CASCADE, verbose_name='ФИО нарушителя', null=True, to_field='id')
    author = models.CharField(max_length=100, verbose_name='ФИО автора')

    change_date = models.DateField(auto_now_add=True, verbose_name='Дата изменения')
    division = models.CharField(max_length=100, verbose_name='Дивизион')
    filial = models.CharField(max_length=200, verbose_name='Филиал')
    representation = models.CharField(verbose_name='Представительство')
    entity = models.CharField(verbose_name='Юридическое лицо')

    description = models.TextField(verbose_name='Описание события')
    way = models.CharField(verbose_name='Тип события', max_length=40)
    instrument = models.CharField(verbose_name='Средство совершения', max_length=100)
    relation = models.CharField(max_length=100, verbose_name='Способ проникновения')
    object = models.CharField(max_length=150, verbose_name='Предмет посягательства')
    place = models.CharField(max_length=300, verbose_name='Место')

    injureds = models.CharField(max_length=300, verbose_name='Пострадавшие', null=True, blank=True)
    witnesses = models.CharField(max_length=300, verbose_name='Свидетели', null=True, blank=True)


    class Meta:
        verbose_name = 'Проишествие'
        verbose_name_plural = 'Проишествия'
        
    def __iter__(self):
        for field in self._meta.fields:
             yield (field.verbose_name,  field.value_to_string(self))

    def __str__(self):
	    return 'ID события: ' + str(self.id) + ' | Дата: ' + str(self.date_incedent)
    

class Injured(models.Model):
    id = models.AutoField(primary_key=True, verbose_name='ID потерпевшего')
    last_name = models.CharField(max_length=30, verbose_name='Фамилия')
    first_name = models.CharField(max_length=30, verbose_name='Имя')
    second_name = models.CharField(max_length=30, verbose_name='Отчество')
    who_is = models.CharField(max_length=200, verbose_name='Кем является:')
    birthday = models.DateField(verbose_name='День рождения', blank=True, null=True)

    class Meta:
        verbose_name = 'Потерпевший'
        verbose_name_plural = 'Потерпевшие'

    def __iter__(self):
        for field in self._meta.fields:
             yield (field.verbose_name,  field.value_to_string(self))

    def __str__(self):
         return self.last_name + ' ' + self.first_name + ' ' + self.second_name
    

class Witness(models.Model):
    id = models.AutoField(primary_key=True, verbose_name='ID свидетеля')
    last_name = models.CharField(max_length=30, verbose_name='Фамилия')
    first_name = models.CharField(max_length=30, verbose_name='Имя')
    second_name = models.CharField(max_length=30, verbose_name='Отчество')
    who_is = models.CharField(max_length=200, verbose_name='Кем является:')
    birthday = models.DateField(verbose_name='День рождения', blank=True, null=True)

    class Meta:
        verbose_name = 'Свидетель'
        verbose_name_plural = 'Свидетели'

    def __iter__(self):
        for field in self._meta.fields:
             yield (field.verbose_name,  field.value_to_string(self))

    def __str__(self):
         return self.last_name + ' ' + self.first_name + ' ' + self.second_name
