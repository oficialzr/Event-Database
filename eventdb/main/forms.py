from django import forms
from .models import Person, Event, Entity, Filial, Division, Representation
from .models import AdressesPlacesOfBirth, AdressesPlacesOfLive, OtherAdresses, AdressesPlacesOfWork



EMPTY_VALUE = [('', '--------')]


class EventForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(EventForm, self).__init__(*args, **kwargs)
        self.fields['entity'].choices = EMPTY_VALUE + sorted(list((i, i) for i in Entity.objects.all().values_list('name', flat=True)))
        self.fields['division'].choices = EMPTY_VALUE + sorted(list((i, i) for i in Division.objects.all().values_list('name', flat=True)))
        self.fields['filial'].choices = EMPTY_VALUE + sorted(list((i, i) for i in Filial.objects.all().values_list('name', flat=True)))
        self.fields['representation'].choices = EMPTY_VALUE + sorted(list((i, i) for i in Representation.objects.all().values_list('name', flat=True)))

    date_incedent = forms.DateTimeField(label='Дата проишествия')
    type = forms.CharField(max_length=100, label='Тип проишествия')

    entity = forms.ChoiceField(label='Юридическое лицо', required=False)
    division = forms.ChoiceField(label='Дивизион', required=False)
    filial = forms.ChoiceField(label='Филиал', required=False)
    representation = forms.ChoiceField(label='Представительство', required=False)

    description = forms.CharField(label='Описание события', widget=forms.Textarea)
    way = forms.CharField(label='Способ проникновения', max_length=40)
    instrument = forms.CharField(label='Средство совершения', max_length=100)
    relation = forms.CharField(max_length=100, label='В отношении')
    object = forms.CharField(max_length=150, label='Предмет посягательства')
    place = forms.CharField(max_length=300, label='Место')

    class Meta:
        model = Event
        exclude = ['id', 'change_date', 'author']


class PersonForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(PersonForm, self).__init__(*args, **kwargs)

    last_name = forms.CharField(max_length=30, label='Фамилия', required=True)
    first_name = forms.CharField(max_length=30, label='Имя', required=True)
    second_name = forms.CharField(max_length=30, label='Отчество', required=True)
    birthday = forms.DateField(label='Дата рождения', required=False)
    sex = forms.CharField(max_length=1, label='Пол (м/ж)', required=False)

    description = forms.CharField(widget=forms.Textarea, label='Описание', required=True)

    class Meta:
        model = Person
        exclude = ['fio', 'add_at', 'id_related', 'author', 'person_image']


class AdressLiveForm(forms.ModelForm):
    class Meta:
        model = AdressesPlacesOfLive
        exclude = ['id_place_of_live', 'who_added']


class AdressOtherForm(forms.ModelForm):
    class Meta:
        model = OtherAdresses
        exclude = ['id_other_places', 'who_added']


class AdressWorkForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(AdressWorkForm, self).__init__(*args, **kwargs)
        self.fields['entity'].choices = EMPTY_VALUE + sorted(list((i, i) for i in Entity.objects.all().values_list('name', flat=True)))
        self.fields['division'].choices = EMPTY_VALUE + sorted(list((i, i) for i in Division.objects.all().values_list('name', flat=True)))
        self.fields['filial'].choices = EMPTY_VALUE + sorted(list((i, i) for i in Filial.objects.all().values_list('name', flat=True)))
        self.fields['representation'].choices = EMPTY_VALUE + sorted(list((i, i) for i in Representation.objects.all().values_list('name', flat=True)))

    entity = forms.ChoiceField(label='Юридическое лицо', required=False)
    division = forms.ChoiceField(label='Дивизион', required=False)
    filial = forms.ChoiceField(label='Филиал', required=False)
    representation = forms.ChoiceField(label='Представительство', required=False)

    class Meta:
        model = AdressesPlacesOfWork
        exclude = ['id_place_of_work', 'who_added']


class AdressBirthForm(forms.ModelForm):
    class Meta:
        model = AdressesPlacesOfBirth
        exclude = ['id_place_of_birth', 'who_added']


class FilterPersonForm(forms.Form):

    def __init__(self, *args, **kwargs):
        super(FilterPersonForm, self).__init__(*args, **kwargs)
        self.fields['entity'].choices = EMPTY_VALUE + list((i, i) for i in Entity.objects.all().values_list('name', flat=True))
        self.fields['division'].choices = EMPTY_VALUE + list((i, i) for i in Division.objects.all().values_list('name', flat=True))
        self.fields['filial'].choices = EMPTY_VALUE + list((i, i) for i in Filial.objects.all().values_list('name', flat=True))
        self.fields['representation'].choices = EMPTY_VALUE + list((i, i) for i in Representation.objects.all().values_list('name', flat=True))

    SEX = [('', 'Нет'), ('м', 'м'), ('ж', 'ж')]
    ROLE = [('', 'Нет'), ('Нарушитель', 'Нарушитель'), ('Свидетель', 'Свидетель'), ('Потерпевший', 'Потерпевший'), ('Другой фигурант', 'Другой фигурант')]

    sex = forms.CharField(label='Пол', required=False, widget=forms.Select(choices=SEX))
    role = forms.CharField(label='Роль лица', required=False, widget=forms.Select(choices=ROLE))
    entity = forms.ChoiceField(label='Юридическое лицо', required=False)
    division = forms.ChoiceField(label='Дивизион', required=False)
    filial = forms.ChoiceField(label='Филиал', required=False)
    representation = forms.ChoiceField(label='Представительство', required=False)

    search_input = forms.CharField(label='search', required=False)


class FilterEventForm(forms.Form):

    def __init__(self, *args, **kwargs):
        super(FilterEventForm, self).__init__(*args, **kwargs)
        self.fields['entity'].choices = EMPTY_VALUE + list((i, i) for i in Entity.objects.all().values_list('name', flat=True))
        self.fields['division'].choices = EMPTY_VALUE + list((i, i) for i in Division.objects.all().values_list('name', flat=True))
        self.fields['filial'].choices = EMPTY_VALUE + list((i, i) for i in Filial.objects.all().values_list('name', flat=True))
        self.fields['representation'].choices = EMPTY_VALUE + list((i, i) for i in Representation.objects.all().values_list('name', flat=True))
        self.fields['type'].choices = EMPTY_VALUE + list((i, i) for i in Event.objects.all().values_list('type', flat=True).distinct())

    type = forms.ChoiceField(label='Вид события', required=False)

    entity = forms.ChoiceField(label='Юридическое лицо', required=False)
    division = forms.ChoiceField(label='Дивизион', required=False)
    filial = forms.ChoiceField(label='Филиал', required=False)
    representation = forms.ChoiceField(label='Представительство', required=False)

    search_input = forms.CharField(label='search', required=False)



