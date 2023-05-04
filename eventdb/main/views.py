import datetime
import json

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.http import JsonResponse

from .models import Violations, Person, RelatedPerson
from .forms import PeopleForm, EventForm

# Views for view data


# login/logout


def loginView(request):
    print(request.POST)
    warning = None
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return JsonResponse(data={'status': 200})
        else:
            warning = 'Введен неправильный логин или пароль!'
            return JsonResponse(data={'status': 500, 'warning': warning})
    return render(request, 'login.html')

def logoutView(request):
    logout(request)
    return redirect('/login')


# main

@login_required
def startPage(request):
    return render(request, 'main-page.html')

@login_required
def eventsView(request):
    violations = Violations.objects.order_by('-id')
    name = 'События'
    name_number = 'События'

    types = set(i[j] for i in violations.values('type') for j in i)

    return render(request, 'home.html', {'violations': violations, 'name': name, 'name_number': name_number, 'event': 1, 'types': types})

@login_required
def personsView(request, role=None):
    if role == 'intruders':
        person = Person.objects.filter(intruder=True)
        name_number = 'Нарушителя'
        name = 'Нарушители'
    elif role == 'witnesses':
        person = Person.objects.filter(witness=True)
        name_number = 'Свидетеля'
        name = 'Свидетели'
    elif role == 'injureds':
        person = Person.objects.filter(injured=True)
        name_number = 'Потерпевшего'
        name = 'Потерпевшие'
    else:
        person = Person.objects.all().order_by('-id')
        name_number = 'Лица'
        name = 'Лица'

    countries = set(i[j] for i in person.values('country') for j in i)
    regions = set(i[j] for i in person.values('region') for j in i)
    return render(request, 'home.html', {'person': person, 
                                         'name_number': name_number, 
                                         'name': name, 
                                         'person_num': 1,
                                         'countries': countries,
                                         'regions': regions,
                                         'author': request.user})


# Views for add data

@login_required
def addEvent(request):
    header = 'Заполните данные о событии'
    if request.method == 'POST':
        form = EventForm(data=request.POST)
        if form.is_valid():
            date_incedent = form.cleaned_data['date_incedent']
            type = form.cleaned_data['type']
            author = form.cleaned_data['author']
            division = form.cleaned_data['division']
            filial = form.cleaned_data['filial']
            representation = form.cleaned_data['representation']
            entity = form.cleaned_data['entity']
            description = form.cleaned_data['description']
            way = form.cleaned_data['way']
            instrument = form.cleaned_data['instrument']
            relation = form.cleaned_data['relation']
            object = form.cleaned_data['object']
            place = form.cleaned_data['place']
            value = Violations(date_incedent=date_incedent, type=type, author=author, division=division, filial=filial, representation=representation, entity=entity, description=description, way=way, instrument=instrument, relation=relation, object=object, place=place)
            value.save()
            request.session['event_id'] = value.id
            return JsonResponse(data=value.id, safe=False)
    else:
        form = EventForm()
        form_person = PeopleForm()
    return render(request, 'add.html', {'form': form, 'form_person': form_person, 'header': header, 'events': 1})

@login_required
def addPersonSolo(request):
    header = 'Заполните данные о человеке'
    if request.method == 'POST':
        form = PeopleForm(data=request.POST)
        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            second_name = form.cleaned_data['second_name']
            description = form.cleaned_data['description']
            sex = form.cleaned_data['sex']
            birthday = form.cleaned_data['birthday']
            country = form.cleaned_data['country']
            area = form.cleaned_data['area']
            locality = form.cleaned_data['locality']
            street = form.cleaned_data['street']
            house = form.cleaned_data['house']
            frame = form.cleaned_data['frame']
            apartment = form.cleaned_data['apartment']
            try:
                a = Person.objects.get(intruder_fio=last_name + ' ' + first_name + ' ' + second_name, birthday=birthday)
                if a:
                    return JsonResponse(data={'message': 'Такой человек уже существует!'})
            except:
                pass

            value = Person(intruder_fio=last_name+' '+first_name+' '+second_name, last_name=last_name, first_name=first_name, second_name=second_name, description=description, sex=sex, birthday=birthday, country=country, area=area, locality=locality, street=street, house=house, frame=frame, apartment=apartment)
            value.save()

            return JsonResponse(data={'status': 200})
            

    else:
        form = PeopleForm()
    return render(request, 'add.html', {'form': form, 'header': header, 'solo': 1})



# /search/?adress=

@login_required
def searchPerson(request):
    intruder = request.GET.get('term')
    intruders = []

    if intruder:
        intruders_list = Person.objects.filter(intruder_fio__iregex=intruder)
        for obj in intruders_list:
            intruders.append(obj.intruder_fio + ' | ' + str(obj.birthday))

    return JsonResponse(intruders, safe=False, json_dumps_params={'ensure_ascii': False}, content_type='application/json; charset=utf-8')

# Views for view persons

@login_required
def eventView(request, event_id):
    event = Violations.objects.get(id=event_id)
    persons = RelatedPerson.objects.filter(id_event=event_id)
    injureds = [Person.objects.get(id=i.id_person) for i in filter(lambda x: x.is_injured, persons)]
    witnesses = [Person.objects.get(id=i.id_person) for i in filter(lambda x: x.is_witness, persons)]
    intruders = [Person.objects.get(id=i.id_person) for i in filter(lambda x: x.is_intruder, persons)]
    
    return render(request, 'event.html', {'event': event, 'persons': persons, 'intruders': intruders, 'injureds': injureds, 'witnesses': witnesses})

@login_required
def personView(request, person_id):
    person = Person.objects.get(id=person_id)
    events = RelatedPerson.objects.filter(id_person=person_id)
    table_name = 'Лицо'
    return render(request, 'person_info.html', {'person': person, 'events': events, 'table_name': table_name})

# add/delete/check person

@login_required
def get_request(request, id):
    data = request.POST
    try: 
        a = data['witness']
        warning = newPeople(data, 2)
    except:
        try:
            a = data['intruder']
            warning = newPeople(data, 1)
        except:
            a = data['injured']
            warning = newPeople(data, 3)
    fio = data['last_name'] + ' ' + data['first_name'] + ' ' + data['second_name']
    birthday = data['birthday']
    if warning:
        return JsonResponse({'warning': warning})
    return JsonResponse({'data': data, 'message': fio + ' | ' + birthday, 'warning': warning}, json_dumps_params={'ensure_ascii': False}, content_type='application/json; charset=utf-8')

@login_required
def check_person(request, id):
    person = request.POST['person']
    try:
        fio, birth = request.POST['person'].split(' | ')
        person_new = Person.objects.get(intruder_fio=fio, birthday=birth)
        return JsonResponse({'person': person_new.__str__()}, json_dumps_params={'ensure_ascii': False}, content_type='application/json; charset=utf-8')
    except Exception as e:
        print(e)
        return JsonResponse({'warning': 'Такого человека не существует!'}, json_dumps_params={'ensure_ascii': False}, content_type='application/json; charset=utf-8')

@login_required
def newPeople(data, role):
    form = PeopleForm(data)
    if form.is_valid():
        first_name = form.cleaned_data['first_name']
        last_name = form.cleaned_data['last_name']
        second_name = form.cleaned_data['second_name']
        description = form.cleaned_data['description']
        sex = form.cleaned_data['sex']
        birthday = form.cleaned_data['birthday']
        country = form.cleaned_data['country']
        region = form.cleaned_data['region']
        area = form.cleaned_data['area']
        locality = form.cleaned_data['locality']
        street = form.cleaned_data['street']
        house = form.cleaned_data['house']
        frame = form.cleaned_data['frame']
        apartment = form.cleaned_data['apartment']

        fio = last_name+' '+first_name+' '+second_name
        try:
            Person.objects.get(intruder_fio=fio, birthday=birthday)
            return 'Такой человек уже существует!\nВыберите человека из списка!'
        except:
            pass

        if role == 1:
            person = Person(intruder_fio=last_name+' '+first_name+' '+second_name, last_name=last_name, first_name=first_name, second_name=second_name, description=description, sex=sex, birthday=birthday, country=country, region=region, area=area, locality=locality, street=street, house=house, frame=frame, apartment=apartment, intruder=True)
        elif role == 2:
            person = Person(intruder_fio=last_name+' '+first_name+' '+second_name, last_name=last_name, first_name=first_name, second_name=second_name, description=description, sex=sex, birthday=birthday, country=country, region=region, area=area, locality=locality, street=street, house=house, frame=frame, apartment=apartment, witness=True)
        elif role == 3:
            person = Person(intruder_fio=last_name+' '+first_name+' '+second_name, last_name=last_name, first_name=first_name, second_name=second_name, description=description, sex=sex, birthday=birthday, country=country, region=region, area=area, locality=locality, street=street, house=house, frame=frame, apartment=apartment, injured=True)

        person.save()
        return False
    
@login_required
def delete_person(request, id):
    fio, birthday = request.POST['person'].split(' | ')
    try:
        person = Person.objects.get(intruder_fio=fio, birthday=birthday)
        if (datetime.datetime.now() - person.add_at).days > 0:
            raise ValueError
        else:
            person.delete()
    except Exception as e:
        return False
    return JsonResponse(data=fio, safe=False, json_dumps_params={'ensure_ascii': False}, content_type='application/json; charset=utf-8')

@login_required
def createRelations(request, event_id):
    event_id = int(request.POST['event_id'])
    if 'intruders' in request.POST:
        intruders = json.loads(request.POST['intruders'])
        for _, value in intruders.items():
            add_relation(value, 1, event_id)
    if 'witnesses' in request.POST:
        witnesses = json.loads(request.POST['witnesses'])
        for _, value in witnesses.items():
            add_relation(value, 2, event_id)
    if 'injureds' in request.POST:
        injureds = json.loads(request.POST['injureds'])
        for _, value in injureds.items():
            add_relation(value, 3, event_id)
    return JsonResponse(data={'status': 200})

@login_required
def add_relation(name, role, event_id):
    fio, birthday = name.split(' | ')
    try:
        if role == 1:
            person = Person.objects.get(intruder_fio=fio, birthday=birthday)
            person.intruder = True
            value = RelatedPerson(id_event=event_id, is_intruder=True, id_person=person.id)
        elif role == 2:
            person = Person.objects.get(intruder_fio=fio, birthday=birthday)
            person.witness = True
            value = RelatedPerson(id_event=event_id, is_witness=True, id_person=person.id)
        elif role == 3:
            person = Person.objects.get(intruder_fio=fio, birthday=birthday)
            person.injured = True
            value = RelatedPerson(id_event=event_id, is_injured=True, id_person=person.id)
        person.save()
        value.save()
    except:
        pass
    return JsonResponse(data={'status': 200})


# tests

@login_required
def testJson(request, event_id):
    person_data = {'name': 'Alex', 'date': '10-02-2002'}
    data = request.GET.dict()
    if not data:
        data['persons'] = []
        data['persons'].append(request.GET)
    else:
        data['persons'].append(data)
    
    return JsonResponse(data=data, json_dumps_params={'ensure_ascii': False}, content_type='application/json; charset=utf-8')


# Views for edit data


# def addPerson(request, event_id, role=None):
#     if role > 3 or not request.session['event_id']:
#         request.session['event_id'] = None
#         return redirect('/events')
#     if role == 1:
#         header = 'заполните данные о нарушителе'
#     elif role == 2:
#         header = 'заполните данные о свидетеле'
#     elif role == 3:
#         header = 'заполните данные о потерпевшем'
#     else:
#         pass

#     if request.method == 'POST':
#         if request.POST['autoComplete']:

#             # Обработка несуществующего лица
#             # ...
            
#             # Обработка существующего лица

#             data = request.POST['autoComplete']
#             fio, date = data.split(' | ')
#             person = Person.objects.get(intruder_fio = fio, birthday=date)
#             try:
#                 # Если связь уже существует
#                 related = RelatedPerson.objects.get(id_event=event_id, id_person=person.id)
#                 if role == 1:
#                     person.intruder = True
#                 elif role == 2:
#                     person.witness = True
#                 elif role == 3:
#                     person.injured = True
#                 person.save()
#                 related.save()
#             except:
#                 # Если связи еще не существует
#                 if role == 1:
#                     related = RelatedPerson(id_event=event_id, id_person=person.id, is_intruder=True)
#                     person.intruder = True
#                 elif role == 2:
#                     related = RelatedPerson(id_event=event_id, id_person=person.id, is_witness=True)
#                     person.witness = True
#                 elif role == 3:
#                     related = RelatedPerson(id_event=event_id, id_person=person.id, is_injured=True)
#                     person.injured = True
#                 related.save()
#                 person.save()
#         else:
#             form = PeopleForm(data=request.POST)
#             if form.is_valid():
#                 first_name = form.cleaned_data['first_name']
#                 last_name = form.cleaned_data['last_name']
#                 second_name = form.cleaned_data['second_name']
#                 description = form.cleaned_data['description']
#                 sex = form.cleaned_data['sex']
#                 birthday = form.cleaned_data['birthday']
#                 country = form.cleaned_data['country']
#                 area = form.cleaned_data['area']
#                 locality = form.cleaned_data['locality']
#                 street = form.cleaned_data['street']
#                 house = form.cleaned_data['house']
#                 frame = form.cleaned_data['frame']
#                 apartment = form.cleaned_data['apartment']

#                 if role == 1:
#                     person = Person(intruder_fio=last_name+' '+first_name+' '+second_name, last_name=last_name, first_name=first_name, second_name=second_name, description=description, sex=sex, birthday=birthday, country=country, region=region, area=area, locality=locality, street=street, house=house, frame=frame, apartment=apartment, intruder=True)
#                     person.save()
#                     related = RelatedPerson(id_event=event_id, id_person=person.id, is_intruder=True)
#                     related.save()
#                 elif role == 2:
#                     person = Person(intruder_fio=last_name+' '+first_name+' '+second_name, last_name=last_name, first_name=first_name, second_name=second_name, description=description, sex=sex, birthday=birthday, country=country, region=region, area=area, locality=locality, street=street, house=house, frame=frame, apartment=apartment, witness=True)
#                     person.save()
#                     related = RelatedPerson(id_event=event_id, id_person=person.id, is_witness=True)
#                     related.save()
#                 elif role == 3:
#                     person = Person(intruder_fio=last_name+' '+first_name+' '+second_name, last_name=last_name, first_name=first_name, second_name=second_name, description=description, sex=sex, birthday=birthday, country=country, region=region, area=area, locality=locality, street=street, house=house, frame=frame, apartment=apartment, injured=True)
#                     person.save()
#                     related = RelatedPerson(id_event=event_id, id_person=person.id, is_injured=True)
#                     related.save()
#         if 'add-more' in request.POST:
#             form = PeopleForm()
#             return render(request, 'add.html', {'form': form, 'header': header, 'role': role})
#         else:
#             return redirect('/add-event/{}/add-person/{}'.format(event_id, role + 1))
#     else:
#         form = PeopleForm()
#     return render(request, 'add.html', {'form': form, 'header': header, 'role': role})





# def addWitness(request, event_id):
#     header = 'заполните данные о нарушителе'
#     if request.method == 'POST':
#         if request.POST['autoComplete']:

#             # Обработка несуществующего лица
#             # ...
            
#             # Обработка существующего лица

#             data = request.POST['autoComplete']
#             fio, date = data.split(' | ')
#             person = Person.objects.get(intruder_fio = fio, birthday=date)
#             try:
#                 # Если связь уже существует
#                 related = RelatedPerson.objects.get(id_event=event_id, id_person=person.id)
#                 related.is_intruder = True
#                 person.intruder = True
#                 person.save()
#                 related.save()
#                 return redirect('/add-')
#             except:
#                 # Если связи еще не существует
#                 related = RelatedPerson(id_event=event_id, id_person=person.id, is_intruder=True)
#                 related.save()
#                 person.intruder = True
#                 person.save()
#                 return redirect('/peoples')
#         else:
#             form = PeopleForm(data=request.POST)
#             if not form.is_valid():
#                 return redirect('/peoples')
#             if form.is_valid():
#                 first_name = form.cleaned_data['first_name']
#                 last_name = form.cleaned_data['last_name']
#                 second_name = form.cleaned_data['second_name']
#                 description = form.cleaned_data['description']
#                 sex = form.cleaned_data['sex']
#                 birthday = form.cleaned_data['birthday']
#                 country = form.cleaned_data['country']
#                 area = form.cleaned_data['area']
#                 locality = form.cleaned_data['locality']
#                 street = form.cleaned_data['street']
#                 house = form.cleaned_data['house']
#                 frame = form.cleaned_data['frame']
#                 apartment = form.cleaned_data['apartment']

#                 person = Person(intruder_fio=last_name+' '+first_name+' '+second_name, last_name=last_name, first_name=first_name, second_name=second_name, description=description, sex=sex, birthday=birthday, country=country, region=region, area=area, locality=locality, street=street, house=house, frame=frame, apartment=apartment, intruder=True)
#                 person.save()
#                 related = RelatedPerson(id_event=event_id, id_person=person.id, is_intruder=True)
#                 related.save()
#                 return redirect('/peoples')
#     else:
#         form = PeopleForm()
#     return render(request, 'add.html', {'form': form, 'header': header})

# def addIntruder(request):
#     header = 'Заполните данные о нарушителе'
#     if request.method == 'POST':
#         form = IntruderForm(data=request.POST)
#         if form.is_valid():
#             first_name = form.cleaned_data['first_name']
#             last_name = form.cleaned_data['last_name']
#             second_name = form.cleaned_data['second_name']
#             description = form.cleaned_data['description']
#             sex = form.cleaned_data['sex']
#             birthday = form.cleaned_data['birthday']
#             with_companion = form.cleaned_data['with_companion']
#             adress_type = form.cleaned_data['adress_type']
#             country = form.cleaned_data['country']
#             area = form.cleaned_data['area']
#             locality = form.cleaned_data['locality']
#             street = form.cleaned_data['street']
#             house = form.cleaned_data['house']
#             frame = form.cleaned_data['frame']
#             apartment = form.cleaned_data['apartment']
#             value = Intruder(intruder_fio=last_name+' '+first_name+' '+second_name, last_name=last_name, first_name=first_name, second_name=second_name, description=description, sex=sex, birthday=birthday, with_companion=with_companion, adress_type=adress_type, country=country, region=region, area=area, locality=locality, street=street, house=house, frame=frame, apartment=apartment)
#             value.save()
#             if request.session['event_id']:
#                 return redirect('/intruders')
#             return redirect('/add-event/')

#             # yyyy-mm-dd
#     else:
#         form = IntruderForm()

#     return render(request, 'add.html', {'form': form, 'header': header})

# def addSoloIntruder(request):
#     header = 'Заполните данные о нарушителе'
#     if request.method == 'POST':
#         form = IntruderForm(data=request.POST)
#         if form.is_valid():
#             first_name = form.cleaned_data['first_name']
#             last_name = form.cleaned_data['last_name']
#             second_name = form.cleaned_data['second_name']
#             description = form.cleaned_data['description']
#             sex = form.cleaned_data['sex']
#             birthday = form.cleaned_data['birthday']
#             with_companion = form.cleaned_data['with_companion']
#             adress_type = form.cleaned_data['adress_type']
#             country = form.cleaned_data['country']
#             area = form.cleaned_data['area']
#             locality = form.cleaned_data['locality']
#             street = form.cleaned_data['street']
#             house = form.cleaned_data['house']
#             frame = form.cleaned_data['frame']
#             apartment = form.cleaned_data['apartment']
#             value = Intruder(intruder_fio=last_name+' '+first_name+' '+second_name, last_name=last_name, first_name=first_name, second_name=second_name, description=description, sex=sex, birthday=birthday, with_companion=with_companion, adress_type=adress_type, country=country, region=region, area=area, locality=locality, street=street, house=house, frame=frame, apartment=apartment)
#             value.save()
#             return redirect('/intruders')

#             # yyyy-mm-dd
#     else:
#         form = IntruderForm()

#     return render(request, 'add.html', {'form': form, 'header': header})


# def addWitness(request):
#     warnings = []
#     header = 'Заполните данные о свидетеле'
#     if request.method == 'POST':
#         form = WitnessForm(data=request.POST)
#         if form.is_valid():
#             if form.cleaned_data['last_name'] == '' and form.cleaned_data['first_name'] == '':
#                 return redirect('/add-injured')
#             last_name = form.cleaned_data['last_name']
#             first_name = form.cleaned_data['first_name']
#             second_name = form.cleaned_data['second_name']
#             who_is = form.cleaned_data['who_is']
#             birthday = form.cleaned_data['birthday']
#             value = Witness(last_name=last_name, first_name=first_name, second_name=second_name, who_is=who_is, birthday=birthday)
#             value.save()
#             event = Violations.objects.get(id=request.session['event_id'])
#             if event.witnesses == None:
#                 event.witnesses = str(value.id)
#                 event.save()
#             else:
#                 event.witnesses = event.witnesses + ',' + str(value.id)
#                 event.save()

#             if 'add-more' in request.POST:
#                 form = WitnessForm()
#                 return render(request, 'add.html', {'form': form, 'header': header, 'id_add': 1})
#             return redirect('/add-injured')

#     else:
#         form = WitnessForm()
#     return render(request, 'add.html', {'form': form, 'header': header, 'id_add': 1})

# def addInjured(request):
#     warnings = []
#     header = 'Заполните данные о потерпевшем'
#     if request.method == 'POST':
#         form = InjuredForm(data=request.POST)
#         if form.is_valid():
#             if form.cleaned_data['last_name'] == '' and form.cleaned_data['first_name'] == '':
#                 return redirect('/')
#             last_name = form.cleaned_data['last_name']
#             first_name = form.cleaned_data['first_name']
#             second_name = form.cleaned_data['second_name']
#             who_is = form.cleaned_data['who_is']
#             birthday = form.cleaned_data['birthday']
#             value = Injured(last_name=last_name, first_name=first_name, second_name=second_name, who_is=who_is, birthday=birthday)
#             value.save()

#             event = Violations.objects.get(id=request.session['event_id'])
#             if event.injureds == None:
#                 event.injureds = str(value.id)
#                 event.save()
#             else:
#                 event.injureds = event.injureds + ',' + str(value.id)
#                 event.save()

#             if 'add-more' in request.POST:
#                 form = InjuredForm()
#                 return render(request, 'add.html', {'form': form, 'header': header, 'id_add': 1})
#             request.session['event_id'] = None
#             return redirect('/')
#     else:
#         form = InjuredForm()
#     return render(request, 'add.html', {'form': form, 'header': header, 'id_add': 2})
