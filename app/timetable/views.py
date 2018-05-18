from django.shortcuts import render

from django.http import JsonResponse
from .models import Timeslot, Room, AKSlot, AK, RoomAssignment

def timetable(request):
    timeslots = Timeslot.objects.all()
    data = {
        'name': 'ZaPF App Database',
        'version': '2.0',
        'slots' : [],
    }

    for t in timeslots:
        slot = {
            "begin": str(t.start)[0:10] + "T" + str(t.start)[11:19] + "+0200", 
            "end": str(t.end)[0:10] + "T" + str(t.end)[11:19] + "+0200", 
            "name": t.name,
            "type": t.event_type
        }
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
    return JsonResponse(data)