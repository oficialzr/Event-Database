import datetime
import json

from django.core import serializers
from django.shortcuts import render, redirect, get_object_or_404, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.forms.models import model_to_dict
from django.core.files.storage import FileSystemStorage

from django.http import JsonResponse

from .models import Event, Person, RelatedPerson, AdressesPlacesOfBirth, AdressesPlacesOfLive, AdressesPlacesOfWork, OtherAdresses, Changes, ChangesEvent, FilesPerson, FilesEvent
from .forms import PersonForm, EventForm, AdressBirthForm, AdressForm, FilterPersonForm, FilterEventForm

# Views for view data


# login/logout


def loginView(request):
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
    form = FilterEventForm(request.GET)
    events = Event.objects.order_by('-id')

    for i, j in request.GET.items():
        if i in ('filial', 'division', 'type'):
            if j:
                events = events.filter(**{i: j})
        if i == 'search_input':
            if j:
                m = j.split()
                events_new = []
                for event in events:
                    if all(x.lower() in event.description.lower() for x in m):
                        events_new.append(event)
                events = events_new

    return render(request, 'home.html', {'events': events,
                                        'name': 'События',
                                        'name_number': 'События',
                                        'event': 1,
                                        'form': form,
                                        'author': request.user.first_name + ' ' + request.user.last_name})

@login_required
def personsView(request):
    form = FilterPersonForm(request.GET)
    persons = Person.objects.order_by('-id')
    if 'role' in request.GET:
        if request.GET['role']:
            persons = list(set(get_object_or_404(Person, id=i.id_person) for i in RelatedPerson.objects.filter(role=request.GET['role'])))
    for i, j in request.GET.items():
        if i == 'role':
            continue
        if i in ('sex', 'filial', 'entity'):
            if i == 'sex':
                if j:
                    m = j
                    persons = filter(lambda x: x.sex==m, persons)
            elif i == 'filial':
                if j:
                    m = j
                    persons = filter(lambda x: AdressesPlacesOfWork.objects.filter(id_place_of_work=x.id, locality=m), persons)
            elif i == 'entity':
                if j:
                    m = j
                    persons = filter(lambda x: AdressesPlacesOfWork.objects.filter(id_place_of_work=x.id, entity=m), persons)
        if i == 'search_input':
            if j:
                m = j.split()
                persons_new = []
                for person in persons:
                    if all(x.lower() in person.fio.lower() for x in m):
                        persons_new.append(person)
                persons = persons_new
    
    return render(request, 'home.html', {'person': persons, 
                                        'name_number': 'Лица', 
                                        'name': 'Лица', 
                                        'person_num': 1,
                                        'author': request.user.first_name + ' ' + request.user.last_name,
                                        'form': form})


# Views for add data

@login_required
def addEvent(request):
    header = 'Заполните данные о событии'
    if request.method == 'POST':
        form = EventForm(data=request.POST)
        if form.is_valid():
            user = User.objects.get(username=request.user)
            author = user.first_name + ' ' + user.last_name
            date_incedent = form.cleaned_data['date_incedent']
            type = form.cleaned_data['type']
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
            value = Event(date_incedent=date_incedent, type=type, author=author, division=division, filial=filial, representation=representation, entity=entity, description=description, way=way, instrument=instrument, relation=relation, object=object, place=place)
            value.save()
            request.session['event_id'] = value.id
            return redirect('/event/'+str(value.id))
    else:
        form = EventForm()
        form_person = PersonForm()
    return render(request, 'add-event.html', {'form': form,
                                              'form_person': form_person,
                                              'header': header,
                                              'events': 1})


@login_required
def addPerson(request, redirected=None):
    header = 'Заполните данные о человеке'
    if request.method == 'POST':
        if 'data' in request.POST:
            try:
                fio, birthday = request.POST['data'].split(' | ')
                person = get_object_or_404(Person, fio=fio, birthday=birthday)
                event_id = request.POST['event_id']
                role = request.POST['role']
                if person:
                    related = RelatedPerson(id_event=event_id, role=role, id_person=person.id)
                    if role == 'Другой фигурант':
                        related.role_desc = request.POST['role_desc']
                        related.save()
                        person.id_related = related.id
                    related.save()
                    person.save()

                    return JsonResponse({'status': '200'})
            except Exception as e:
                return JsonResponse({'status': '404'})
        else:
            form = PersonForm(data=request.POST)
            if form.is_valid():
                user = User.objects.get(username=request.user)
                author = user.first_name + ' ' + user.last_name
                first_name = form.cleaned_data['first_name']
                last_name = form.cleaned_data['last_name']
                second_name = form.cleaned_data['second_name']
                description = form.cleaned_data['description']
                sex = form.cleaned_data['sex']
                birthday = form.cleaned_data['birthday']
                
                try:
                    a = Person.objects.get(fio=last_name + ' ' + first_name + ' ' + second_name, birthday=birthday)
                    if a:
                        return JsonResponse(data={'message': 'Такой человек уже существует!'})
                except:
                    pass

                value = Person(fio=last_name+' '+first_name+' '+second_name, last_name=last_name, first_name=first_name, second_name=second_name, description=description, sex=sex, birthday=birthday, author=author)
                value.save()
                if 'redirected' in request.POST:
                    return JsonResponse({'redirect': '200'})
                else:
                    return JsonResponse({'status': '200', 'id': value.id})      
    else:
        form = PersonForm()
    if redirected:
        return render(request, 'add-person.html', {'form': form,
                                               'header': header,
                                               'redirected': 1})
    else:
        return render(request, 'add-person.html', {'form': form,
                                               'header': header})


@login_required
def add_person_with_redirect(request):
    return addPerson(request, True)


@login_required
def addAdress(request, person_id):
    if request.method == 'POST':
        if 'adress' in request.POST:
            form = AdressBirthForm(data=request.POST)
        else:
            form = AdressForm(data=request.POST)
        role = request.POST['role']
        print(role)
        if form.is_valid():
            if role == '1':
                adress = form.cleaned_data['adress']
                country = form.cleaned_data['country']
                region = form.cleaned_data['region']

                value = AdressesPlacesOfBirth(country=country, region=region, adress=adress, id_place_of_birth=Person(id=person_id), who_added=request.user.last_name+' '+request.user.first_name)
            else:
                description = form.cleaned_data['description']
                country = form.cleaned_data['country']
                region = form.cleaned_data['region']
                area = form.cleaned_data['area']
                locality = form.cleaned_data['locality']
                street = form.cleaned_data['street']
                house = form.cleaned_data['house']
                frame = form.cleaned_data['frame']
                apartment = form.cleaned_data['apartment']

                entity = form.cleaned_data['entity']
                if role == '2':
                    value = AdressesPlacesOfWork(id_place_of_work=Person(id=person_id), country=country, region=region, area=area, locality=locality, street=street, house=house, frame=frame, apartment=apartment, who_added=request.user.last_name+' '+request.user.first_name, entity=entity)
                elif role == '3':
                    value = AdressesPlacesOfLive(id_place_of_live=Person(id=person_id), country=country, region=region, area=area, locality=locality, street=street, house=house, frame=frame, apartment=apartment, who_added=request.user.last_name+' '+request.user.first_name)
                elif role == '4':
                    value = OtherAdresses(id_other_places=Person(id=person_id), description=description, country=country, region=region, area=area, locality=locality, street=street, house=house, frame=frame, apartment=apartment, who_added=request.user.last_name+' '+request.user.first_name)

            value.save()
        return JsonResponse(data={'status': 200, 'data': serializers.serialize('json', [value])})
    else:
        form_adress = AdressForm()
        form_birth = AdressBirthForm()


    return render(request, 'add-adress.html', {
        'form_adress': form_adress,
        'form_birth': form_birth,
        'person_id': person_id
    })


@login_required
def add_person_on_event(request, id):
    form = PersonForm()
    return render(request, 'add-person-on-event.html', {'form_person': form,
                                                        'event_id': id}) 






# VIEWS FOR EDIT

@login_required
def edit_person(request, id_person):
    if request.method == 'POST':
        desc = request.POST.get('description')
        person = get_object_or_404(Person, id=id_person)
        change_value = Changes(id_user=request.user.id, edit_from=person.description, edit_to=desc, type_edit='Описание', id_record=person.id, record_name='Лицо')
        change_value.save()

        person.description = desc
        person.save()


        return redirect(f'/person/{id_person}')
    else:
        model = model_to_dict(Person.objects.get(id=id_person))
        model['birthday'] = datetime.datetime.strftime(model['birthday'], '%Y-%m-%d')
        form = PersonForm(model)
    return render(request, 'edit.html', {'form': form,
                                         'header': 'лица',
                                         'person': 1})


@login_required
def edit_event(request, id_event):
    if request.method == 'POST':
        edit_from = json.dumps(model_to_dict(Event.objects.get(id=id_event)), ensure_ascii=False, default=str)
        event = get_object_or_404(Event, id=id_event)
        description = request.POST['description']
        way = request.POST['way']
        instrument = request.POST['instrument']
        relation = request.POST['relation']
        object = request.POST['object']
        place = request.POST['place']

        event.description = description
        event.way = way
        event.instrument = instrument
        event.relation = relation
        event.object = object
        event.place = place

        event.save()

        edit_to = json.dumps(model_to_dict(Event.objects.get(id=id_event)), ensure_ascii=False, default=str)

        if not edit_from == edit_to:
            change_value = ChangesEvent(id_user=request.user.id, edit_from=edit_from, edit_to=edit_to, id_record=id_event, record_name='Событие')
            change_value.save()


        return redirect(f'/event/{id_event}')
    else:
        model = model_to_dict(Event.objects.get(id=id_event))
        model['date_incedent'] = datetime.datetime.strftime(model['date_incedent'], '%Y-%m-%d %H:%M')
        form = EventForm(model)
    return render(request, 'edit.html', {'form': form,
                                         'header': 'события',
                                         'event': 1})








# /search/?term=

@login_required
def searchPerson(request):
    person = request.GET.get('term')
    persons = []

    if person:
        intruders_list = Person.objects.filter(fio__iregex=person)
        for obj in intruders_list:
            persons.append(obj.fio + ' | ' + str(obj.birthday))

    return JsonResponse({'status': 200, 'data': persons}, json_dumps_params={'ensure_ascii': False}, content_type='application/json; charset=utf-8')









# Views for view event/person

@login_required
def eventView(request, event_id):
    if request.method == 'POST' and request.FILES:
        event = Event.objects.get(id=event_id)

        if 'file' in request.FILES:
            file = request.FILES['file']
            filename = file.name
            value = FilesEvent(event_id=event_id, file=file, filename=filename)
            value.save()


        event.save()
        return redirect('../event/{}'.format(event_id))
    
    files = FilesEvent.objects.filter(event_id=event_id)
    event = Event.objects.get(id=event_id)
    persons = RelatedPerson.objects.filter(id_event=event_id)
    injureds = [Person.objects.get(id=i.id_person) for i in persons if i.role == 'Потерпевший']
    witnesses = [Person.objects.get(id=i.id_person) for i in persons if i.role == 'Свидетель']
    intruders = [Person.objects.get(id=i.id_person) for i in persons if i.role == 'Нарушитель']
    others = [{'i': Person.objects.get(id=i.id_person), 'j': i.role_desc} for i in persons if i.role == 'Другой фигурант']

    persons_list = [{'persons': intruders, 'name': 'Нарушители'},
                    {'persons': witnesses, 'name': 'Свидетели'},
                    {'persons': injureds, 'name': 'Потерпевшие'},
                    {'persons': others, 'name': 'Остальные фигуранты'}
               ]

    if request.user.username == 'root':
        changes = ChangesEvent.objects.filter(id_record=event_id)
    else:
        changes = ChangesEvent.objects.filter(id_record=event_id, id_user=request.user.id)

    return render(request, 'event.html', {'event': event, 
                                          'persons_list': persons_list,
                                          'event_id': event_id,
                                          'changes': changes,
                                          'files': files})

@login_required
def personView(request, person_id):
    if request.method == 'POST' and request.FILES:
        person = Person.objects.get(id=person_id)

        if 'image' in request.FILES:
            image = request.FILES['image']
            person.person_image = image
        else:
            file = request.FILES['file']
            filename = file.name
            value = FilesPerson(person_id=person_id, file=file, filename=filename)
            value.save()


        person.save()
        return redirect('../person/{}'.format(person_id))

    person = Person.objects.get(id=person_id)
    image = person.person_image
    files = FilesPerson.objects.filter(person_id=person_id)
    events = RelatedPerson.objects.filter(id_person=person_id)
    try:
        places_of_birth = AdressesPlacesOfBirth.objects.filter(id_place_of_birth=person.id)
        places_of_work = AdressesPlacesOfWork.objects.filter(id_place_of_work=person.id)
        places_of_live = AdressesPlacesOfLive.objects.filter(id_place_of_live=person.id)
        other_places = OtherAdresses.objects.filter(id_other_places=person.id)
    except:
        places_of_birth = None
        places_of_work = None
        places_of_live = None
        other_places = None

    places = [{'place': places_of_birth, 'name': 'Место рождения:'}, 
              {'place': places_of_work, 'name': 'Место работы:'},
              {'place': places_of_live, 'name': 'Адрес регистрации:'},
              {'place': other_places, 'name': 'Остальные адреса:'}]

    if request.user.username == 'root':
        changes = Changes.objects.filter(id_record=person_id)
    else:
        changes = Changes.objects.filter(id_record=person_id, id_user=request.user.id)

    table_name = 'Лицо'

    return render(request, 'person_info.html', {'person': person, 'events': events, 'table_name': table_name,
                                                'places': places,
                                                'changes': changes,
                                                'image': image,
                                                'files': files})


@login_required
def changeView(request, change_id):
    change = get_object_or_404(ChangesEvent, id=change_id)
    change_from = json.loads(change.edit_from).items
    change_to = json.loads(change.edit_to).items
    return render(request, 'change-page.html', {'change_from': change_from,
                                                'change_to': change_to})






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
