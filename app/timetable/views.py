from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
import arrow
from django.http import JsonResponse
from .models import Timeslot, Room, AKSlot, AK, RoomAssignment, News

def index(request):
    template = loader.get_template('index.html')
    return HttpResponse(template.render({}, request))

def timetable(request):
    timeslots = Timeslot.objects.all()
    data = {
        'name': 'ZaPF App Database',
        'version': '2.0',
        'news': [{"date": arrow.get(n.time).humanize(locale='de_de'), "msg": n.message} for n in News.objects.all()],
        'slots' : [],
    }

    for t in timeslots:
        slot = {
            "begin": arrow.get(t.start).format('ddd HH:mm', locale='de_de'), 
            "end": arrow.get(t.end).format('HH:mm'),
            "timestamp": int(arrow.get(t.start).timestamp),
            "finish": str(t.end)[0:10] + "T" + str(t.end)[11:19] + "+0200",  
            "name": t.name,
            "type": t.event_type
        }
        if t.place:
            slot["place"] = t.place
        if hasattr(t, 'akslot'):
            slot["aks"] = []
            for ak in t.akslot.ak_set.all():
                ak_set = {
                    "name": ak.name,
                    "responsible": ak.responsible,
                    "room": ak.room.name,
                    "url": ak.url,
                }
                slot["aks"].append(ak_set)
        data["slots"].append(slot)
        #"aks" : [x for x in t.akslot.ak_set.all() if t]
    data['slots'].sort(key=lambda x: x['timestamp'])
    return JsonResponse(data)