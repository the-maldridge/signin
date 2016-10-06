from django.forms import formset_factory
from django.shortcuts import render, redirect
from django.http import HttpResponse

import datetime

from .models import Person
from .models import Timeslot

from .forms import NewUserForm

def index(request):
    people = Person.objects.filter(active=True)
    present = Timeslot.objects.filter(time_out=None)

    p_present = []
    for person in present:
        p_present.append(person.person)

    # Make people contain only people that aren't signed in
    people = list(set(people)-set(p_present))
    return render(request, "index.html.j2", {"people":people, "present":p_present})

def tap_in(request, person_id):
    t = Timeslot()
    # safe to assert since pk must have a single result
    t.person = Person.objects.filter(pk=person_id)[0]
    t.time_in = datetime.datetime.now()
    t.save()
    return redirect(index)

def tap_out(request, person_id):
    t = Timeslot.objects.filter(time_out=None)
    for slot in t:
        if slot.person.pk == int(person_id):
            slot.time_out = datetime.datetime.now()
            slot.save()
            return redirect(index)
    return HttpResponse("Tried to sign out someone who isn't here!?")

def log(request):
    t = Timeslot.objects.all()
    return render(request, "log.html.j2", {"log":t})

def new(request):
    if request.method == 'GET':
        form = NewUserForm()
        return render(request, "new.html.j2", {"form":form})
    else:
        p = NewUserForm(request.POST)
        p.save()
        return redirect(index)
