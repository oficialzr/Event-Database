from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.core import serializers

from .models import Violations, Intruder, Witness, Injured
from .forms import IntruderForm, EventForm, WitnessForm, InjuredForm

# Views for view data

def startPage(request):
    violations = Violations.objects.order_by('-id')
    name = 'События'
    name_number = 'События'
    return render(request, 'home.html', {'violations': violations, 'name': name, 'name_number': name_number})

def injuredsView(request):
    people = Injured.objects.order_by('-id')
    name_number = 'Потерпевшего'
    name = 'Потерпевшие'
    return render(request, 'home.html', {'people': people, 'name_number': name_number, 'name': name, 'injured': 1})

def witnessView(request):
    people = Witness.objects.order_by('-id')
    name_number = 'Свитеделя'
    name = 'Свидетели'
    return render(request, 'home.html', {'people': people, 'name_number': name_number, 'name': name, 'witness': 1})

def intrudersView(request):
    intruders = Intruder.objects.order_by('-id')
    name_number = 'Нарушителя'
    name = 'Нарушители'
    return render(request, 'home.html', {'intruders': intruders, 'name_number': name_number, 'name': name, 'intruders_id': 1})


# Views for add data

def addIntruder(request):
    header = 'Заполните данные о нарушителе'
    if request.method == 'POST':
        form = IntruderForm(data=request.POST)
        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            second_name = form.cleaned_data['second_name']
            description = form.cleaned_data['description']
            sex = form.cleaned_data['sex']
            birthday = form.cleaned_data['birthday']
            with_companion = form.cleaned_data['with_companion']
            adress_type = form.cleaned_data['adress_type']
            country = form.cleaned_data['country']
            region = form.cleaned_data['region']
            area = form.cleaned_data['area']
            locality = form.cleaned_data['locality']
            street = form.cleaned_data['street']
            house = form.cleaned_data['house']
            frame = form.cleaned_data['frame']
            apartment = form.cleaned_data['apartment']
            value = Intruder(intruder_fio=last_name+' '+first_name+' '+second_name, last_name=last_name, first_name=first_name, second_name=second_name, description=description, sex=sex, birthday=birthday, with_companion=with_companion, adress_type=adress_type, country=country, region=region, area=area, locality=locality, street=street, house=house, frame=frame, apartment=apartment)
            value.save()
            return redirect('/add-event/')

            # yyyy-mm-dd
    else:
        form = IntruderForm()

    return render(request, 'add.html', {'form': form, 'header': header})

def addSoloIntruder(request):
    header = 'Заполните данные о нарушителе'
    if request.method == 'POST':
        form = IntruderForm(data=request.POST)
        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            second_name = form.cleaned_data['second_name']
            description = form.cleaned_data['description']
            sex = form.cleaned_data['sex']
            birthday = form.cleaned_data['birthday']
            with_companion = form.cleaned_data['with_companion']
            adress_type = form.cleaned_data['adress_type']
            country = form.cleaned_data['country']
            region = form.cleaned_data['region']
            area = form.cleaned_data['area']
            locality = form.cleaned_data['locality']
            street = form.cleaned_data['street']
            house = form.cleaned_data['house']
            frame = form.cleaned_data['frame']
            apartment = form.cleaned_data['apartment']
            value = Intruder(intruder_fio=last_name+' '+first_name+' '+second_name, last_name=last_name, first_name=first_name, second_name=second_name, description=description, sex=sex, birthday=birthday, with_companion=with_companion, adress_type=adress_type, country=country, region=region, area=area, locality=locality, street=street, house=house, frame=frame, apartment=apartment)
            value.save()
            return redirect('/intruders')

            # yyyy-mm-dd
    else:
        form = IntruderForm()

    return render(request, 'add.html', {'form': form, 'header': header})

def addEvent(request):
    warnings = []
    header = 'Заполните данные о событии'
    if request.method == 'POST':
        form = EventForm(data=request.POST)
        if form.is_valid():
            try:
                Intruder.objects.get(intruder_fio=form.cleaned_data['intruder'])
            except:
                warnings.append('Нарушитель не найден. Введите верное значение из выпадающего списка')
            date_incedent = form.cleaned_data['date_incedent']
            type = form.cleaned_data['type']
            intruder = form.cleaned_data['intruder']
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
            if warnings:
                return render(request, 'add.html', {'form': form, 'header': header, 'warnings': warnings})
            value = Violations(date_incedent=date_incedent, type=type, intruder=Intruder.objects.get(intruder_fio=intruder), author=author, division=division, filial=filial, representation=representation, entity=entity, description=description, way=way, instrument=instrument, relation=relation, object=object, place=place)
            value.save()
            request.session['event_id'] = value.id
            return redirect('/add-witness')
    else:
        form = EventForm()
    return render(request, 'add.html', {'form': form, 'header': header})

def addWitness(request):
    warnings = []
    header = 'Заполните данные о свидетеле'
    if request.method == 'POST':
        form = WitnessForm(data=request.POST)
        if form.is_valid():
            if form.cleaned_data['last_name'] == '' and form.cleaned_data['first_name'] == '':
                return redirect('/add-injured')
            last_name = form.cleaned_data['last_name']
            first_name = form.cleaned_data['first_name']
            second_name = form.cleaned_data['second_name']
            who_is = form.cleaned_data['who_is']
            birthday = form.cleaned_data['birthday']
            value = Witness(last_name=last_name, first_name=first_name, second_name=second_name, who_is=who_is, birthday=birthday)
            value.save()
            event = Violations.objects.get(id=request.session['event_id'])
            if event.witnesses == None:
                event.witnesses = str(value.id)
                event.save()
            else:
                event.witnesses = event.witnesses + ',' + str(value.id)
                event.save()

            if 'add-more' in request.POST:
                form = WitnessForm()
                return render(request, 'add.html', {'form': form, 'header': header, 'id_add': 1})
            return redirect('/add-injured')

    else:
        form = WitnessForm()
    return render(request, 'add.html', {'form': form, 'header': header, 'id_add': 1})

def addInjured(request):
    warnings = []
    header = 'Заполните данные о потерпевшем'
    if request.method == 'POST':
        form = InjuredForm(data=request.POST)
        if form.is_valid():
            if form.cleaned_data['last_name'] == '' and form.cleaned_data['first_name'] == '':
                return redirect('/')
            last_name = form.cleaned_data['last_name']
            first_name = form.cleaned_data['first_name']
            second_name = form.cleaned_data['second_name']
            who_is = form.cleaned_data['who_is']
            birthday = form.cleaned_data['birthday']
            value = Injured(last_name=last_name, first_name=first_name, second_name=second_name, who_is=who_is, birthday=birthday)
            value.save()

            event = Violations.objects.get(id=request.session['event_id'])
            if event.injureds == None:
                event.injureds = str(value.id)
                event.save()
            else:
                event.injureds = event.injureds + ',' + str(value.id)
                event.save()

            if 'add-more' in request.POST:
                form = InjuredForm()
                return render(request, 'add.html', {'form': form, 'header': header, 'id_add': 1})
            request.session['event_id'] = None
            return redirect('/')
    else:
        form = InjuredForm()
    return render(request, 'add.html', {'form': form, 'header': header, 'id_add': 2})


# /search/?adress=

def searchIntruder(request):
    intruder = request.GET.get('intruder')

    intruders = []

    if intruder:
        intruders_objs = Intruder.objects.filter(intruder_fio__iregex=intruder)
        for obj in intruders_objs:
            intruders.append(obj.intruder_fio)

    return JsonResponse({'status': 200, 'data': intruders}, json_dumps_params={'ensure_ascii': False}, content_type='application/json; charset=utf-8')


# Views for view persons


def eventView(request, event_id):
    event = Violations.objects.get(id=event_id)
    intruder = Intruder.objects.get(id=event.intruder_id)
    try:
        injureds = [Injured.objects.get(id=int(i)) for i in event.injureds.split(',')]
    except:
        injureds = []
    try:
        witnesses = [Witness.objects.get(id=int(i)) for i in event.witnesses.split(',')]
    except:
        witnesses = []
    return render(request, 'event.html', {'event': event, 'intruder': intruder, 'injureds': injureds, 'witnesses': witnesses})

def injuredPersonView(request, injured_id):
    person = Injured.objects.get(id=injured_id)
    events = Violations.objects.filter(injureds__icontains=injured_id)
    table_name = 'Потерпевший'
    return render(request, 'person_info.html', {'person': person, 'events': events, 'table_name': table_name})

def witnessPersonView(request, witness_id):
    person = Witness.objects.get(id=witness_id)
    events = Violations.objects.filter(witnesses__icontains=witness_id)
    table_name = 'Свидетель'
    return render(request, 'person_info.html', {'person': person, 'events': events, 'table_name': table_name})

def intruderPersonView(request, intruder_id):
    person = Intruder.objects.get(id=intruder_id)
    events = Violations.objects.filter(intruder=intruder_id)
    table_name = 'Нарушитель'
    return render(request, 'person_info.html', {'person': person, 'events': events, 'table_name': table_name})


# Views for edit data

def editIntruder(request, intruder_id):
    if request.method == 'POST':
        form = IntruderForm(data=request.POST)
        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            second_name = form.cleaned_data['second_name']
            description = form.cleaned_data['description']
            sex = form.cleaned_data['sex']
            birthday = form.cleaned_data['birthday']
            with_companion = form.cleaned_data['with_companion']
            adress_type = form.cleaned_data['adress_type']
            country = form.cleaned_data['country']
            region = form.cleaned_data['region']
            area = form.cleaned_data['area']
            locality = form.cleaned_data['locality']
            street = form.cleaned_data['street']
            house = form.cleaned_data['house']
            frame = form.cleaned_data['frame']
            apartment = form.cleaned_data['apartment']
            value = Intruder(intruder_fio=last_name+' '+first_name+' '+second_name, last_name=last_name, first_name=first_name, second_name=second_name, description=description, sex=sex, birthday=birthday, with_companion=with_companion, adress_type=adress_type, country=country, region=region, area=area, locality=locality, street=street, house=house, frame=frame, apartment=apartment)
            value.save()
            return redirect('/intruders/')
    else:
        person = Intruder.objects.get(id=intruder_id)
        form = IntruderForm()

    return render(request, 'edit.html', {'form': form, 'person': person})


