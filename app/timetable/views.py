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
        try:
            slot["place"] = t.place
        except:
            pass
            
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

def try_else(_input, _else):

    try:
        result = _input
        return result
    except:
        return _else

def ak_table(request):
    aks = AK.objects.all()
    rooms = Room.objects.all()
    akslots = AKSlot.objects.all()

    data = [[{"room": room.name, "akslot": "", "responsible": "", "name": ""} for akslot in akslots] for room in rooms]
    print(data)

    rooms_result = []

    rooms_id_dict = {}
    for i, room in enumerate(rooms):
        rooms_id_dict[room.id] = i
        rooms_result.append(room.name)


    akslots_result = []

    akslots_id_dict = {}
    for i, akslot in enumerate(akslots):
        akslots_id_dict[akslot.id] = i 
        akslots_result.append(akslot.name)

    for i, ak in enumerate(aks):
        try:
            data[rooms_id_dict[ak.room.id]][akslots_id_dict[ak.akslot.id]]["room"] = ak.room.name
        except:
            pass

        try:
            data[rooms_id_dict[ak.room.id]][akslots_id_dict[ak.akslot.id]]["akslot"] = ak.akslot.name
        except:
            pass

        try:
            data[rooms_id_dict[ak.room.id]][akslots_id_dict[ak.akslot.id]]["responsible"] = ak.responsible
        except:
            pass

        try:
            data[rooms_id_dict[ak.room.id]][akslots_id_dict[ak.akslot.id]]["name"] = ak.name
        except:
            pass

        try:
            data[rooms_id_dict[ak.room.id]][akslots_id_dict[ak.akslot.id]]["short"] = ak.short
        except:
            pass

        try:
            data[rooms_id_dict[ak.room.id]][akslots_id_dict[ak.akslot.id]]["kleine_fachschaften"] = ak.kleine_fachschaften
        except:
            pass
            
        try:
            data[rooms_id_dict[ak.room.id]][akslots_id_dict[ak.akslot.id]]["ak"] = True
        except:
            pass

        # data[rooms_id_dict[ak.room.id]][akslots_id_dict[ak.akslot.id]] = {
        #     "room": ak.room.name,
        #     "akslot": ak.akslot.name,
        #     "responsible": ak.responsible,
        #     "name": ak.name,
        #     "short": ak.short,
        # }
    x = {"data": data, "rooms": rooms_result, "akslots": akslots}
    print(x)

    template = loader.get_template('ak_table.html')
    return HttpResponse(template.render(x, request))