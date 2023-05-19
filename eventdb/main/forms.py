from django import forms
from .models import Person, AdressesPlacesOfWork, Event


class EventForm(forms.Form):
    date_incedent = forms.DateTimeField(label='Дата проишествия (Формат даты: YYYY-MM-DD HH:MM)')
    type = forms.CharField(max_length=100, label='Тип проишествия')

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



class PersonForm(forms.Form):
    last_name = forms.CharField(max_length=30, label='Фамилия', required=True)
    first_name = forms.CharField(max_length=30, label='Имя', required=True)
    second_name = forms.CharField(max_length=30, label='Отчество', required=True)
    birthday = forms.DateField(label='Дата рождения', required=False)
    sex = forms.CharField(max_length=1, label='Пол (м/ж)', required=False)

    description = forms.CharField(widget=forms.Textarea, label='Описание', required=True)


class AdressForm(forms.Form):
    entity = forms.CharField(label='Юридическое лицо', required=False)
    description = forms.CharField(label='Описание адреса', required=False)
    country = forms.CharField(label='Страна', required=True)
    region = forms.CharField(label='Область', required=False)
    area = forms.CharField(label='Район', required=False)
    locality = forms.CharField(label='Населенный пункт', required=False)
    street = forms.CharField(label='Улица', required=False)
    house = forms.CharField(label='Дом', required=False)
    frame = forms.CharField(label='Корпус', required=False)
    apartment = forms.CharField(label='Квартира', required=False)


class AdressBirthForm(forms.Form):
    country = forms.CharField(label='Страна', required=True)
    region = forms.CharField(label='Область', required=False)
    adress = forms.CharField(label='Адрес', required=False, widget=forms.Textarea)


class FilterPersonForm(forms.Form):
    SEX = [('', 'Нет'), ('м', 'м'), ('ж', 'ж')]
    ROLE = [('', 'Нет'), ('Нарушитель', 'Нарушитель'), ('Свидетель', 'Свидетель'), ('Потерпевший', 'Потерпевший'), ('Другой фигурант', 'Другой фигурант')]
    FILIALS = [('', 'Нет')] + [(i['locality'], i['locality']) for i in AdressesPlacesOfWork.objects.all().values('locality').distinct()]

    sex = forms.CharField(label='Пол', required=False, widget=forms.Select(choices=SEX))
    role = forms.CharField(label='Роль лица', required=False, widget=forms.Select(choices=ROLE))
    filial = forms.CharField(label='Филиал', required=False, widget=forms.Select(choices=FILIALS))
    entity = forms.ModelChoiceField(label='Юридическое лицо', required=False, queryset=AdressesPlacesOfWork.objects.all().values_list('entity', flat=True).distinct(), empty_label='Нет')

    search_input = forms.CharField(label='search', required=False)


class FilterEventForm(forms.Form):
    type = forms.ModelChoiceField(label='Вид события', queryset=Event.objects.all().values_list('type', flat=True).distinct(), empty_label='Нет', required=False)
    division = forms.ModelChoiceField(label='Дивизион', queryset=Event.objects.all().values_list('division', flat=True).distinct(), empty_label='Нет', required=False)
    filial = forms.ModelChoiceField(label='Филиал', queryset=Event.objects.all().values_list('filial', flat=True).distinct(), empty_label='Нет', required=False)

    search_input = forms.CharField(label='search', required=False)



