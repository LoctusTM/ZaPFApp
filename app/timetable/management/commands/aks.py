import numpy as np
import random
import operator

from django.core.management.base import BaseCommand
from timetable.models import Timeslot, Room, AKSlot, AK, RoomAssignment, News
from constance import config


def n_t(n, k):
    return (n%k, n//k)

def t_n(x1, x2, k):
    return x1 + x2* k

def wh(array, val):
    return np.argwhere(array==val)[0][0], np.argwhere(array==val)[0][1]


Räume = config.rooms
Zeitslots = config.timeslots


"""
aks = np.arange(1, AKs+1).astype(int)
raum_zeit = np.zeros((Zeitslots, Räume)) # 8 Räume, 7 Zeitslots
raum_zeit.astype(int)

aks2 = aks.copy()
aks2 = np.append(aks2, np.zeros(Räume*Zeitslots-AKs))

results = []

for k in range(100):
    random.shuffle(aks2)
    
    for i, ak in enumerate(aks2):
        raum_zeit[n_t(i, Zeitslots)[0]][n_t(i, Zeitslots)[1]] = ak
    
    kleine_fachschaften = np.zeros((Zeitslots, Räume))
    
    for x, y in [(x, 1) for x in kleine_fachschaften_aks]:
        kleine_fachschaften[wh(raum_zeit, x)] = y
        
    badness = len((np.argwhere(np.count_nonzero(kleine_fachschaften, 1)>1)))
    
    results.append((badness, raum_zeit, kleine_fachschaften))
"""

class Command(BaseCommand):
    args = '<foo bar ...>'
    help = ''

    def _timeslot_assignment(self):
        r = Room.objects.filter(hörsaal=False)
        a = AK.objects.filter(backup=False)
        s = AKSlot.objects.filter(backup=False)

        print(r)


        Räume = len(r)
        Zeitslots = len(s)

        kleine_fachschaften_aks = [(i, ak.kleine_fachschaften) for i, ak in enumerate(a)]

        aks = np.arange(1, len(a)+1).astype(int)
        raum_zeit = np.zeros((Zeitslots, Räume)) # 8 Räume, 7 Zeitslots
        raum_zeit.astype(int)

        aks2 = aks.copy()
        aks2 = np.append(aks2, np.zeros(Räume*Zeitslots-len(a)))


        ###################

        r2 = Room.objects.all()
        a2 = AK.objects.all()
        s2 = AKSlot.objects.all()
        Räume2 = len(r2)
        Zeitslots2 = len(s2)
        aks3 = np.arange(1, len(a2)+1).astype(int)
        raum_zeit2 = np.zeros((Zeitslots2, Räume2))
        raum_zeit2.astype(int)
        aks4 = aks3.copy()
        aks4 = np.append(aks4, np.zeros(Räume2*Zeitslots2-len(a2)))

        results2 = []

        for i, ak in enumerate(aks4):
            raum_zeit2[n_t(i, Zeitslots2)[0]][n_t(i, Zeitslots2)[1]] = ak

        results2.append((0, raum_zeit2, 0))


        ###################

        results = []

        for k in range(100):
            random.shuffle(aks2)
            
            for i, ak in enumerate(aks2):
                raum_zeit[n_t(i, Zeitslots)[0]][n_t(i, Zeitslots)[1]] = ak
            
            kleine_fachschaften = np.zeros((Zeitslots, Räume))
            
            for x, y in kleine_fachschaften_aks:
                kleine_fachschaften[wh(raum_zeit, x)] = y
                
            badness = len((np.argwhere(np.count_nonzero(kleine_fachschaften, 1)>1)))
            
            results.append((badness, raum_zeit, kleine_fachschaften))
        results.sort(key=lambda tup: tup[0])

        rr = [room for room in Room.objects.all()]
        aa = [akslot for akslot in AKSlot.objects.all()]

        n = 0
        for i, slot in enumerate(results[0][1]):
            for j, ak in enumerate(slot):
                if int(ak) != 0:
                    ak_elem = a2[int(ak)-1]
                    
                    ak_elem.room = r[j]
                    ak_elem.akslot = s2[i]
                    k, l = rr.index(r[j]), aa.index(s2[i])
                    ak_elem.public_id = l*Räume2 + k
                    ak_elem.save()

                n += 1

                #ak_elem = a2[int(k+l*results2[0][1].shape[1])]


    def handle(self, *args, **options):
        self._timeslot_assignment()