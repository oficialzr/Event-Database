from django import forms


class IntruderForm(forms.Form):
    last_name = forms.CharField(label='Фамилия', max_length=30, required=False)
    first_name = forms.CharField(label='Имя', max_length=30, required=False)
    second_name = forms.CharField(max_length=30, label='Отчество', required=False)
    description = forms.CharField(label='Описание нарушителя (Обязательное поле)', widget=forms.Textarea)
    sex = forms.CharField(max_length=1, label='Пол (м/ж)', required=False)
    birthday = forms.DateField(label='День рождения (Формат даты: YYYY-MM-DD)', required=False)
    with_companion = forms.CharField(label='В компании с:', required=False)
    adress_type = forms.CharField(label='Тип адреса', required=False)
    country = forms.CharField(label='Страна', required=False)
    region = forms.CharField(label='Область', required=False)
    area = forms.CharField(label='Район', required=False)
    locality = forms.CharField(label='Населенный пункт', required=False)
    street = forms.CharField(label='Улица', required=False)
    house = forms.CharField(label='Дом', required=False)
    frame = forms.CharField(label='Корпус', required=False)
    apartment = forms.CharField(label='Квартира', required=False)

class EventForm(forms.Form):
    date_incedent = forms.DateField(label='Дата проишествия (Формат даты: YYYY-MM-DD)')
    type = forms.CharField(max_length=100, label='Тип проишествия')
    author = forms.CharField(max_length=100, label='ФИО автора')

    division = forms.CharField(max_length=100, label='Дивизион')
    filial = forms.CharField(max_length=200, label='Филиал')
    representation = forms.CharField(label='Представительство')
    entity = forms.CharField(label='Юридическое лицо')

    description = forms.CharField(label='Описание события', widget=forms.Textarea)
    way = forms.CharField(label='Способ проникновения', max_length=40)
    instrument = forms.CharField(label='Средство совершения', max_length=100)
    relation = forms.CharField(max_length=100, label='В отношении')
    object = forms.CharField(max_length=150, label='Предмет посягательства')
    place = forms.CharField(max_length=300, label='Место')


class WitnessForm(forms.Form):
    last_name = forms.CharField(label='Фамилия', max_length=30, required=False)
    first_name = forms.CharField(label='Имя', max_length=30, required=False)
    second_name = forms.CharField(max_length=30, label='Отчество', required=False)
    who_is = forms.CharField(max_length=200, label='Кем является:', required=False)
    birthday = forms.DateField(label='День рождения', required=False)


class InjuredForm(forms.Form):
    last_name = forms.CharField(label='Фамилия', max_length=30, required=False)
    first_name = forms.CharField(label='Имя', max_length=30, required=False)
    second_name = forms.CharField(max_length=30, label='Отчество', required=False)
    who_is = forms.CharField(max_length=200, label='Кем является:', required=False)
    birthday = forms.DateField(label='День рождения', required=False)


class PeopleForm(forms.Form):
    last_name = forms.CharField(max_length=30, label='Фамилия', required=True)
    first_name = forms.CharField(max_length=30, label='Имя', required=True)
    second_name = forms.CharField(max_length=30, label='Отчество', required=True)
    description = forms.CharField(widget=forms.Textarea, label='Описание', required=True)
    sex = forms.CharField(max_length=1, label='Пол (м/ж)', required=False)
    birthday = forms.DateField(label='Дата рождения', required=False)
    country = forms.CharField(label='Страна', required=False)
    region = forms.CharField(label='Область', required=False)
    area = forms.CharField(label='Район', required=False)
    locality = forms.CharField(label='Населенный пункт', required=False)
    street = forms.CharField(label='Улица', required=False)
    house = forms.CharField(label='Дом', required=False)
    frame = forms.CharField(label='Корпус', required=False)
    apartment = forms.CharField(label='Квартира', required=False)

    # injured = forms.BooleanField(label='Потерпевший', required=False)
    # intruder = forms.BooleanField(label='Нарушитель', required=False)
    # witness = forms.BooleanField(label='Свидетель', required=False)
