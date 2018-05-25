from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
import arrow
from django.http import JsonResponse
from .models import Timeslot, Room, AKSlot, AK, RoomAssignment, News
from .forms import ChangeForm
from django.contrib.admin.views.decorators import staff_member_required



def n_t(n, k):
    return (n%k, n//k)

def t_n(x1, x2, k):
    return x1 + x2* k

def wh(array, val):
    return np.argwhere(array==val)[0][0], np.argwhere(array==val)[0][1]

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
                if ak.published == True:
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

@staff_member_required
def ak_table(request):
    aks = AK.objects.all()
    rooms = Room.objects.all()
    akslots = AKSlot.objects.all()

    Räume = len(rooms)
    Slots = len(akslots)

    data = [[{"room": rooms[i].name, "akslot": "", "responsible": "", "name": "", "public_id": j*len(rooms)+i} for j in range(len(akslots))] for i in range(len(rooms))]

    if request.method == 'POST':
        form = ChangeForm(request.POST)
        if form.is_valid():
            slot_1 = int(form.cleaned_data['slot_1'])
            slot_2 = int(form.cleaned_data['slot_2'])  

            a = AK.objects.filter(public_id=slot_1)
            b = AK.objects.filter(public_id=slot_2)

            if len(a) == 1 and len(b) == 1:
                a[0].public_id, b[0].public_id = b[0].public_id, a[0].public_id
                a[0].akslot, b[0].akslot = b[0].akslot, a[0].akslot
                a[0].room, b[0].room = b[0].room, a[0].room
                a[0].save()
                b[0].save()
                print("a")

            """

            if len(a) == 1 and len(b) == 0:
                a[0].public_id = slot_2
                a[0].akslot = akslots[slot_2//Räume]
                a[0].raum = rooms[slot_2%Slots]
                a[0].save()
                print("b", a[0].akslot)

            if len(a) == 0 and len(b) == 1:
                b[0].public_id = slot_1
                b[0].akslot = akslots[slot_1//Räume]
                b[0].raum = rooms[slot_1%Slots]
                b[0].save()
                print("c")

            """

            return HttpResponseRedirect('/aktable/')

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

        try:
            data[rooms_id_dict[ak.room.id]][akslots_id_dict[ak.akslot.id]]["id"] = ak.id
        except:
            pass

        try:
            data[rooms_id_dict[ak.room.id]][akslots_id_dict[ak.akslot.id]]["public_id"] = ak.public_id
        except:
            pass

        # data[rooms_id_dict[ak.room.id]][akslots_id_dict[ak.akslot.id]] = {
        #     "room": ak.room.name,
        #     "akslot": ak.akslot.name,
        #     "responsible": ak.responsible,
        #     "name": ak.name,
        #     "short": ak.short,
        # }
    form = ChangeForm()
    x = {"data": data, "rooms": rooms_result, "akslots": akslots, 'form': form}

    template = loader.get_template('ak_table.html')
    return HttpResponse(template.render(x, request))

